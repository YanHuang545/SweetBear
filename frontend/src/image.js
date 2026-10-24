export function thumbUrl(url, size = 400) {
  if (!url) return "";
  let href = url;
  if (href.startsWith("//")) href = "https:" + href;
  if (href.startsWith("http://")) href = "https://" + href.slice(7);
  if (!/alicdn\.com|taobaocdn\.com|tbcdn\.cn/.test(href)) return href;
  const base = href.split("?")[0];
  if (/_\d+x\d+/.test(base)) return href;
  return `${base}_${size}x${size}q75.jpg_.webp`;
}
