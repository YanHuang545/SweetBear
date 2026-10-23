import hashlib
import json
import sys
import time

import requests

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

APP_KEY = "34839810"
URL = "https://h5api.m.goofish.com/h5/mtop.taobao.idlemtopsearch.pc.search/1.0/"
REQUIRED_COOKIES = ("cookie2", "_m_h5_tk", "_m_h5_tk_enc")
BX_UA = "234!5I4eKS29eeP4I96Wu75L8LNwzMyXZb0So2TRGeFH5rHbTs3vwk8m/jtS3jUd3ZeN8M8vD47s7JxXpNryHsAmNHZVF+LHuAlfY1RVz2nGyVFsJZYiNAm7PVCEZYB0vUvmQmKbIfm3ybTb9gXlisJe2SzsaMKpsOGRtE+wFnP+UrnZn3UH9AJ7hwFeOWcOCdeRXKjOQmdNirLZZ3wH9idThpoZnkp/cAjenL5cQCyN02cZn3UH94erkUcZOks/c24HVnoHOQ6NhstZZ3wd9iJTCP2ZQkk8gsyHVZodOQhNhscQZ0Wd9iy6CPr+8pkpcs4HjVWzQCyNhsrkZ3wd9ibACPV+/3kCc2r7nZodQCymhxuZVkUd9AdJhLoZQQikl35iZ3oHQQVmhskZVw4uok14hL0IQps/cuWWP5CdQUNyJxqkVow08AT/fOZZHpiZc247n3odQQVNwynZj4UWzjEXBt8BP4kXc247ZZoHQQVmhxkZnE4+2o+NOARsoNvDCdHUePkbWoOnaPa2S3lAEjE2WaCc+jvbEPYBB3L2J7Pq2HDxiZf1t7yAa4FutNcREUTuSpLfT1hJATTxvZG75iD+aghsJDvVarevX3IfJFLbfbF/8Bvpt1Q2kEmjDjO/EV4O49SfTjYVeHR/OiG7KGv+axmcmq5jgy4O59hSCAeRuLP/ACZIFhPW3de7CagHXBjR48wmZJH9GC+AQJMbrjc6FwQgcUlpMe6QEjgCt7z0JURWUpeihgMjkRDN8dRDCZx+i6AgQiHTGs1RrvYapPelbsrogXU/jNF47xqtaQUMiQYy8DBk79smfHDjCCQOOh4cT7gnfIX5MfOmBD5r185QHiQ/ff3PBm4gnbDbZKwGSEZ3LHXn49v2NBVM7u68RRswsQPJOMPQ663sGJPemU471gql0kyj5Mo0fW7jauHghnFROJzJjQdrOg9seCR4plQs4w5ASemqUDPwyvtfVNjQT/PwJECFzVjtos3p0cGdxjKhOQ3s11yg6bCpwACMKvGUCBSGGPQhT6qRW7PDggf1yd/eP2aEoEkPYE9oIgc7YYrHw83VMTclAMG7lo8lfisLaMt3TzUbyPi7wOFeH6UYZ5yy2hfApHUESQ3rlYLZp0iKvx28zcFQEbmVCxCa8gI6f+06MIhIJxL34F6qolLONJGgphn8hxuPnzYrfEvY/96jHVDEnoaC0kms39eHTax6O5DBnt3Y259IGPWk9b9RDNSoZAj2SfkYluAjFZqEA3ICPy0/i9YCcP1hVexz3Lfo3MDSmL+R+TPrnWjoVZadblrGCwl+VRkmoOuOUmQtfaM0d9Mo+MDrOV1XSyO+l4+PlbfOLb8CtQ9R3/cghl721yUjHr6GrOst3oRaeS2cxLMRpx4+Jgb/Ufeygl3mSQsxUvMzXyTfXho70f3H6INZVwK5XDbDE6jOeYt3UKh/+FPDMPn3/c219nKRWY6D3oeH+POAAkyPcyugMJPhgPU5q/Nw3QJjFh5Xuh20ztXaS5VbBaezjW/quQbIe3MW5mhSGtCqa7fcWBoC8isqJEB712yeCZ7870Wp59Uwi2zGMt0MLqkm9aTHGECSjJtLP64auir4BIRx/+h/a8I2HOPOLbEb3ONimm49qlK7"
BX_UMIDTOKEN = "T2gAVqQJa1QI7Rcm6ytEiti401wlUdn9KjurrigpWSWkyEoOTzHPGSLJ5hiSqOFfXpI="
BX_ET = "gJ6mnJMnjsRjTf0zKVJbW_Kg_EP8lK96wNH9WdLaaU8SkqHAbVbGzwIxHOIwSNbJPxCYGCLijK6RMALYldjNJd4LJJedci9BQyUKxBl5Fp-n_jutggkyBh05Xs0hci96Q03a9_SbsjNV0xJN7LRycHvw0Al4qL-Bmdk2_xlrzUtwQd820UkychMquEkaqg8Wbdk20NSzqhLy7dJN7glREj8dQ6Wzg9tdpQLPoTxc4csuNAkggnup-iPrIAWlgnLUpUDZQTxcfowtevV986Tv9F_zexvG4hbk9s4nnNjNA1RlIqrA8Gfl5KBzbj8FMZdGHQ0qgHvDoBW2amDVcC5lEKB45XsRqERHe_F7kCpco6TBg7a5SgYA7tArozLO9gB2Zwz-ENOG_tpP3zyh4ocrTtOIC3rOUfG6g3tkJhbjcMwjeK-YqucdfI-WAeEuqfG6g3tkJuqo9sO2VHTd."

COOKIES = {
    "cookie2": "",
    "_m_h5_tk": "",
    "_m_h5_tk_enc": "",
}
KEYWORD = "PS5光盘"
PAGE_NUMBER = 2


class CookieError(ValueError):
    pass


def parse_cookie_string(raw):
    parsed = {}
    for part in (raw or "").split(";"):
        piece = part.strip()
        if not piece or "=" not in piece:
            continue
        key, value = piece.split("=", 1)
        parsed[key.strip()] = value.strip()
    missing = [name for name in REQUIRED_COOKIES if not parsed.get(name)]
    if missing:
        raise CookieError("missing cookies: " + ", ".join(missing))
    return {
        "cookie2": parsed["cookie2"],
        "_m_h5_tk": parsed["_m_h5_tk"],
        "_m_h5_tk_enc": parsed["_m_h5_tk_enc"],
        "tracknick": parsed.get("tracknick") or "guest",
    }


def cookies_to_string(cookies):
    return "; ".join(f"{key}={value}" for key, value in cookies.items())


def _https(url):
    if not url:
        return ""
    if url.startswith("http://"):
        return "https://" + url[len("http://") :]
    if url.startswith("//"):
        return "https:" + url
    return url


def parse_item(card):
    main = ((card.get("data") or {}).get("item") or {}).get("main") or {}
    ex = main.get("exContent") or {}
    detail = ex.get("detailParams") or {}
    title = (
        ex.get("title")
        or (ex.get("titleSpan") or {}).get("content")
        or detail.get("title")
        or ""
    )
    title = " ".join(str(title).split())
    price_parts = ex.get("price") or []
    price = "".join(
        part.get("text", "")
        for part in price_parts
        if isinstance(part, dict)
    )
    if not price:
        price = str(detail.get("soldPrice") or "")
    price = price.replace("¥", "").replace("￥", "").strip()
    item_id = str(ex.get("itemId") or detail.get("itemId") or "")
    return {
        "id": item_id,
        "title": title,
        "price": price,
        "area": ex.get("area") or "",
        "picUrl": _https(ex.get("picUrl") or detail.get("picUrl") or ""),
    }


def search_page(cookie_string, keyword, page_number=1, rows_per_page=30):
    cookies = parse_cookie_string(cookie_string)
    search_data = {
        "pageNumber": int(page_number),
        "keyword": keyword,
        "fromFilter": False,
        "rowsPerPage": int(rows_per_page),
        "sortValue": "",
        "sortField": "",
        "customDistance": "",
        "gps": "",
        "propValueStr": {},
        "customGps": "",
        "searchReqFromPage": "pcSearch",
        "extraFilterValue": "{}",
        "userPositionJson": "{}",
    }
    token = cookies["_m_h5_tk"].split("_", 1)[0]
    t = str(int(time.time() * 1000))
    data_str = json.dumps(search_data, ensure_ascii=False, separators=(",", ":"))
    sign = hashlib.md5(f"{token}&{t}&{APP_KEY}&{data_str}".encode("utf-8")).hexdigest()
    payload = requests.post(
        URL,
        cookies={
            "cookie2": cookies["cookie2"],
            "_m_h5_tk": cookies["_m_h5_tk"],
            "_m_h5_tk_enc": cookies["_m_h5_tk_enc"],
        },
        params={
            "appKey": APP_KEY,
            "t": t,
            "sign": sign,
            "spm_cnt": "a21ybx.search.0.0",
            "spm_pre": "a21ybx.search.searchInput.0",
        },
        data={
            "data": data_str,
            "bx-ua": BX_UA,
            "bx-umidtoken": BX_UMIDTOKEN,
            "bx_et": BX_ET,
        },
        timeout=20,
    ).json()
    ret = payload.get("ret") or []
    items = [parse_item(card) for card in (payload.get("data") or {}).get("resultList") or []]
    for item in items:
        if not item["id"]:
            item["id"] = str(abs(hash(item["title"] + item["price"])))
    return {
        "ret": ret,
        "ok": bool(ret) and str(ret[0]).startswith("SUCCESS"),
        "nick": cookies["tracknick"],
        "keyword": keyword,
        "pageNumber": int(page_number),
        "items": items,
    }


def print_cli():
    result = search_page(cookies_to_string(COOKIES), KEYWORD, PAGE_NUMBER)
    if not result["ok"]:
        print(result["ret"])
    items = result["items"]
    print(f"第{result['pageNumber']}页，共{len(items)}条")
    for index, item in enumerate(items, start=1):
        title = item["title"]
        if len(title) > 40:
            title = title[:40] + "..."
        print(f"{index}.商品名称：{title},价格：{item['price']}块")


def serve():
    from flask import Flask, jsonify, request
    from flask_cors import CORS

    app = Flask(__name__)
    CORS(app)

    @app.get("/api/health")
    def health():
        return jsonify({"ok": True, "name": "Tianxiong"})

    @app.post("/api/login")
    def login():
        body = request.get_json(silent=True) or {}
        cookie = (body.get("cookie") or "").strip()
        try:
            parsed = parse_cookie_string(cookie)
        except CookieError as exc:
            return jsonify({"ok": False, "error": str(exc)}), 400
        return jsonify({"ok": True, "nick": parsed["tracknick"]})

    @app.post("/api/search")
    def search():
        body = request.get_json(silent=True) or {}
        cookie = (body.get("cookie") or "").strip()
        keyword = (body.get("keyword") or "").strip()
        page_number = body.get("pageNumber") or 1
        if not keyword:
            return jsonify({"ok": False, "error": "keyword required"}), 400
        try:
            result = search_page(cookie, keyword, page_number)
        except CookieError as exc:
            return jsonify({"ok": False, "error": str(exc)}), 400
        except Exception as exc:
            return jsonify({"ok": False, "error": str(exc)}), 502
        return jsonify(result), (200 if result["ok"] else 400)

    app.run(host="127.0.0.1", port=8787, debug=False)


if __name__ == "__main__":
    if sys.argv[1:] == ["serve"]:
        serve()
    else:
        print_cli()
