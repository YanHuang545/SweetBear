import { clearCookie } from "./session";

function rawMessage(payload) {
  return payload.error || (payload.ret && payload.ret[0]) || "请求失败";
}

function friendlyError(raw) {
  const text = String(raw || "");
  if (/TOKEN_EXOIRED|TOKEN_EXPIRED/i.test(text)) {
    return "闲鱼令牌过期，请到 www.goofish.com 重新复制整段 Cookie 再贴进来";
  }
  if (/TOKEN_EMPTY/i.test(text)) {
    return "Cookie 里缺少有效的 _m_h5_tk，请复制完整一段";
  }
  if (/RGV587/i.test(text)) {
    return "闲鱼风控拦了一下，换一份刚复制的 Cookie 或稍后再试";
  }
  if (/missing cookies/i.test(text)) {
    return "至少要包含 cookie2、_m_h5_tk、_m_h5_tk_enc";
  }
  if (/NameResolutionError|getaddrinfo|Failed to resolve|HTTPSConnectionPool/i.test(text)) {
    return "连不上闲鱼接口，检查网络后点再试一次。";
  }
  if (/Max retries|timed out|Timeout|Connection/i.test(text)) {
    return "闲鱼接口暂时连不上，过几秒再搜一次。";
  }
  return text;
}

function tokenDead(raw) {
  return /TOKEN_EXOIRED|TOKEN_EXPIRED|TOKEN_EMPTY/i.test(String(raw || ""));
}

async function post(path, body) {
  const response = await fetch(path, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body),
  });
  const payload = await response.json();
  if (!response.ok || payload.ok === false) {
    const raw = rawMessage(payload);
    if (tokenDead(raw) && !window.location.pathname.startsWith("/login")) {
      clearCookie();
      window.location.replace(
        "/login?reason=" + encodeURIComponent(friendlyError(raw)),
      );
    }
    throw new Error(friendlyError(raw));
  }
  return payload;
}

export function login(cookie) {
  return post("/api/login", { cookie });
}

export function searchItems(cookie, keyword, pageNumber) {
  return post("/api/search", { cookie, keyword, pageNumber });
}
