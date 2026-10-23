const COOKIE_KEY = "tianxiong.cookie";
const ITEM_KEY = "tianxiong.item";

export function getCookie() {
  return localStorage.getItem(COOKIE_KEY) || "";
}

export function setCookie(value) {
  localStorage.setItem(COOKIE_KEY, value);
}

export function clearCookie() {
  localStorage.removeItem(COOKIE_KEY);
}

export function nickFromCookie(raw = getCookie()) {
  const match = raw.match(/tracknick=([^;]+)/);
  return match ? decodeURIComponent(match[1]) : "甜熊客人";
}

export function saveItem(item) {
  sessionStorage.setItem(ITEM_KEY, JSON.stringify(item));
}

export function loadItem() {
  try {
    return JSON.parse(sessionStorage.getItem(ITEM_KEY) || "null");
  } catch {
    return null;
  }
}

export function loadList(key, fallback) {
  try {
    return JSON.parse(localStorage.getItem(key) || "") || fallback;
  } catch {
    return fallback;
  }
}

export function saveList(key, value) {
  localStorage.setItem(key, JSON.stringify(value));
}
