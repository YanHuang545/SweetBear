async function post(path, body) {
  const response = await fetch(path, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body),
  });
  const payload = await response.json();
  if (!response.ok || payload.ok === false) {
    throw new Error(payload.error || (payload.ret && payload.ret[0]) || "请求失败");
  }
  return payload;
}

export function login(cookie) {
  return post("/api/login", { cookie });
}

export function searchItems(cookie, keyword, pageNumber) {
  return post("/api/search", { cookie, keyword, pageNumber });
}
