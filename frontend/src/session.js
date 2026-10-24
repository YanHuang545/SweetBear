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

const ITEMS_KEY = "tianxiong.items";

export function saveItem(item) {
  sessionStorage.setItem(ITEM_KEY, JSON.stringify(item));
  if (!item?.id) return;
  const all = loadItemMap();
  all[item.id] = item;
  sessionStorage.setItem(ITEMS_KEY, JSON.stringify(all));
}

export function loadItem() {
  try {
    return JSON.parse(sessionStorage.getItem(ITEM_KEY) || "null");
  } catch {
    return null;
  }
}

export function loadItemById(id) {
  if (!id) return null;
  const current = loadItem();
  if (current && String(current.id) === String(id)) return current;
  return loadItemMap()[id] || loadItemMap()[String(id)] || null;
}

function loadItemMap() {
  try {
    return JSON.parse(sessionStorage.getItem(ITEMS_KEY) || "{}") || {};
  } catch {
    return {};
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

const LAST_SEARCH_KEY = "tianxiong.lastSearch";

export function saveLastSearch(keyword) {
  sessionStorage.setItem(LAST_SEARCH_KEY, keyword || "");
}

export function lastListPath() {
  const keyword = sessionStorage.getItem(LAST_SEARCH_KEY) || "";
  return keyword ? `/search?q=${encodeURIComponent(keyword)}` : "/";
}

export function lastItemPath() {
  const item = loadItem();
  return item?.id ? `/item/${item.id}` : lastListPath();
}
