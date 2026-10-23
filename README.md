# Tianxiong (甜熊)

Personal reverse-engineering lab for **Goofish** (闲鱼) PC search, plus a local Vue 3 storefront named **Tianxiong**.

This is a study project. It is **not** an official Goofish / Xianyu product, not a mini-program, and not a hosted service. Use only **your own** logged-in browser session.

## What is in the repo

| Path | Role |
| --- | --- |
| `request.py` | One Python entry: signed mtop search (CLI) and the Flask proxy (`serve`). |
| `requirements.txt` | Python deps: `requests`, `flask`, `flask-cors`. |
| `frontend/` | Vue 3 + Vite app **Tianxiong** — candy-shelf UI, cookie-paste login, no QR code. |
| `.gitignore` | Ignores `__pycache__/`, venv, `frontend/node_modules/`, `.env`. |

`request.py` does both jobs:

```bash
py -3 request.py         # print titles and prices
py -3 request.py serve   # Flask API on 127.0.0.1:8787 for the Vue app
```

Tianxiong pages:

- **Login** — paste your Goofish cookie string
- **Home / Search** — live listings via the proxy
- **Item** — detail from the search card
- **Publish / Messages / Orders / Profile** — full UI; those flows are stored in `localStorage` because those APIs were not wired

The visual language is cocoa, cream, and berry candy cards with a left rail. It is intentionally not a yellow 闲鱼 clone.

## Architecture

```text
Browser (Vue 3, :5173)
    POST /api/login  /api/search
            |
Vite proxy (/api → 127.0.0.1:8787)
            |
request.py serve  (Flask)
    parse cookie2 + _m_h5_tk + _m_h5_tk_enc
    sign = md5(token + "&" + t + "&" + appKey + "&" + dataJSON)
            |
Goofish mtop search
```

CLI mode (`py -3 request.py`) calls the same `search_page()` helper. Edit `COOKIES`, `KEYWORD`, and `PAGE_NUMBER` at the top of `request.py`.

`sign` can be computed locally. Login cookies cannot. `cookie2` and `_m_h5_tk` are issued after you log in to Goofish in a real browser. `_m_h5_tk` expires; when mtop returns `FAIL_SYS_TOKEN_EXOIRED`, paste a fresh cookie string.

## Reverse-engineering notes

Worked from a **live PC search** on `https://www.goofish.com/search`, with DevTools capturing `POST /h5/mtop.taobao.idlemtopsearch.pc.search/1.0/`.

1. **Capture, then strip.** Replay the captured Python request, then drop headers / cookies / query params one by one. Empty cookies → `RGV587`. Missing `_m_h5_tk` → `FAIL_SYS_TOKEN_EMPTY`. Empirically the search still succeeds with only `cookie2` + `_m_h5_tk` + `_m_h5_tk_enc`, plus query `appKey`, `t`, `sign`, `spm_cnt`, `spm_pre`. Most browser headers are optional.
2. **`sign` is mtop H5, not a secret in the search JSON.** In `lib-mtop` 2.7.x (`__processRequestUrl` / `__getTokenFromCookie`):

   ```text
   token = _m_h5_tk.split("_")[0]
   t     = Date.now()            # milliseconds, same value as query t
   data  = JSON.stringify(body)  # compact, no spaces
   sign  = md5(token + "&" + t + "&" + appKey + "&" + data)
   ```

   `appKey` for this PC site is `34839810`. Changing only `pageNumber` (or `keyword` / `rowsPerPage`) without recomputing `sign` returns `FAIL_SYS_ILLEGAL_ACCESS`. `sign` does **not** include `bx-ua` / `bx-umidtoken` / `bx_et`.
3. **Who sends what.** Business code (`lib.mtop.request`) posts `data` (and used to send `ua`). **Baxia** then hooks XHR (`paramsType: ["uab","umid","et"]`) and appends:

   | Field | SDK | Behavior |
   | --- | --- | --- |
   | `bx-ua` | AWSC fireyejs (`234!…`) via `baxiaCommon.getUA()` | New fingerprint every request |
   | `bx-umidtoken` | fireyejs `getUidToken()`, seeded by `ynuf.aliapp.org/service/um.json` | Stable inside one session |
   | `bx_et` | AWSC ET `et_f.js` → `__awsc_et__.getETToken()` | New token every request |

   These are environment tickets, not hashes you can derive like `sign`. `request.py` replays captured values; they go stale under risk control.
4. **Session lifetime.** `cookie2` is a login session cookie. `_m_h5_tk` looks like `hex_expiryMs` and is refreshed when mtop answers `FAIL_SYS_TOKEN_EXOIRED` with `Set-Cookie`. Closing the Goofish tab does not immediately kill a still-valid cookie, but an expired tk will.
5. **Pagination / keyword.** Same endpoint. Only the search JSON body changes; resign with a fresh `t`. Hammering the API quickly can hit `RGV587_ERROR` (rate / crowd control).

## Requirements

- Python 3.10+ (developed with 3.14)
- Node.js 18+
- A Goofish PC session that belongs to you

```bash
py -3 -m pip install -r requirements.txt
cd frontend
npm install
```

## Run the CLI search

In `request.py`, set `KEYWORD` and `PAGE_NUMBER`, put your three cookies in the `COOKIES` dict, then:

```bash
py -3 request.py
```

It prints compact lines like:

```text
第1页，共30条
1.商品名称：…,价格：…块
```

## Run Tianxiong

Terminal 1:

```bash
py -3 request.py serve
```

Terminal 2:

```bash
cd frontend
npm run dev
```

Open [http://localhost:5173](http://localhost:5173). Paste your cookie string into **“把钥匙放进糖罐”**. No QR scan.

## Cookie string

From Chrome DevTools → Application → Cookies (or the request Cookie header) on `www.goofish.com`, copy the full `name=value; ...` string.

The proxy only **requires**:

- `cookie2`
- `_m_h5_tk`
- `_m_h5_tk_enc`

`tracknick` is optional and is shown as the nickname.

Do not commit live cookies. Strip values in `request.py` before you push.

## Disclaimer

- Use this only against **your own** account for learning.
- Do not farm cookies, share sessions, or run this as a public search API.
- Goofish risk-control fields (`bx-ua`, `bx-umidtoken`, `bx_et`) are environment tickets from the official JS SDKs. Replaying captured values is enough for a short local demo and will go stale.
- Official product work needs official APIs, not this stack.
