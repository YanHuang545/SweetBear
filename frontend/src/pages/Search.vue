<template>
  <AppShell>
    <PageBack to="/" label="返回首页" />
    <div class="page-head">
      <p class="page-kicker">搜索结果</p>
      <h1>{{ keyword || "全部" }}</h1>
    </div>
    <p v-if="error" class="error">
      {{ error }}
      <button class="btn ghost" type="button" :disabled="loading" @click="load">再试一次</button>
    </p>
    <p v-else-if="loading && !items.length" class="meta">正在加载…</p>
    <div v-if="items.length" class="grid" :class="{ dimmed: loading }">
      <CandyCard
        v-for="(item, index) in items"
        :key="item.id"
        :item="item"
        :priority="index < 8"
        @open="openItem"
      />
    </div>
    <div class="pager">
      <button class="page-num" :disabled="page <= 1 || loading" @click="goTo(page - 1)">‹</button>
      <button
        v-for="(slot, index) in pageSlots"
        :key="`${slot}-${index}`"
        class="page-num"
        :class="{ active: slot === page, dots: slot === '…' }"
        :disabled="loading || slot === '…'"
        @click="slot !== '…' && goTo(slot)"
      >
        {{ slot }}
      </button>
      <button class="page-num" :disabled="!hasMore || loading" @click="goTo(page + 1)">›</button>
      <form class="pager-jump" @submit.prevent="jump">
        <span class="meta">跳到</span>
        <input v-model="jumpValue" type="number" min="1" inputmode="numeric" />
        <button class="btn ghost" type="submit" :disabled="loading">页</button>
      </form>
    </div>
  </AppShell>
</template>

<script setup>
import { computed, ref, watch } from "vue";
import { useRoute, useRouter } from "vue-router";
import AppShell from "../layouts/AppShell.vue";
import PageBack from "../components/PageBack.vue";
import CandyCard from "../components/CandyCard.vue";
import { searchItems } from "../api";
import { getCookie, saveItem, saveLastSearch } from "../session";

const PAGE_SIZE = 30;
const route = useRoute();
const router = useRouter();
const items = ref([]);
const error = ref("");
const loading = ref(false);
const page = ref(1);
const keyword = ref("");
const jumpValue = ref("1");
const hasMore = ref(false);
const cache = new Map();
let loadSeq = 0;

function cacheKey(keyword, pageNumber) {
  return `${keyword}|${pageNumber}`;
}

function applyResult(result, pageNumber) {
  items.value = result.items;
  hasMore.value = result.items.length >= PAGE_SIZE;
  jumpValue.value = String(pageNumber);
  if (!result.items.length) error.value = "这一页没有商品";
}

function prefetch(keyword, pageNumber) {
  const key = cacheKey(keyword, pageNumber);
  if (cache.has(key)) return;
  searchItems(getCookie(), keyword, pageNumber)
    .then((result) => {
      if (cache.size > 20) cache.delete(cache.keys().next().value);
      cache.set(key, result);
    })
    .catch(() => {});
}

const pageSlots = computed(() => {
  const current = page.value;
  const last = hasMore.value ? Math.max(current + 2, 5) : current;
  if (last <= 7) {
    return Array.from({ length: last }, (_, index) => index + 1);
  }
  const marks = new Set([1, last, current]);
  for (let n = current - 2; n <= current + 2; n += 1) {
    if (n >= 1 && n <= last) marks.add(n);
  }
  const nums = [...marks].sort((a, b) => a - b);
  const slots = [];
  let prev = 0;
  for (const n of nums) {
    if (prev && n - prev > 1) slots.push("…");
    slots.push(n);
    prev = n;
  }
  return slots;
});

async function load() {
  keyword.value = String(route.query.q || "数码");
  saveLastSearch(keyword.value);
  page.value = Number(route.query.page || 1);
  const seq = ++loadSeq;
  const key = cacheKey(keyword.value, page.value);
  error.value = "";
  const cached = cache.get(key);
  if (cached) {
    applyResult(cached, page.value);
    loading.value = false;
    prefetch(keyword.value, page.value + 1);
    return;
  }
  loading.value = true;
  try {
    const result = await searchItems(getCookie(), keyword.value, page.value);
    if (seq !== loadSeq) return;
    if (cache.size > 20) cache.delete(cache.keys().next().value);
    cache.set(key, result);
    applyResult(result, page.value);
    prefetch(keyword.value, page.value + 1);
  } catch (err) {
    if (seq !== loadSeq) return;
    error.value = err.message;
    if (!items.value.length) hasMore.value = false;
  } finally {
    if (seq === loadSeq) loading.value = false;
  }
}

function goTo(next) {
  const target = Math.max(1, Number(next) || 1);
  if (target === page.value) return;
  router.push({ path: "/search", query: { q: keyword.value, page: String(target) } });
}

function jump() {
  goTo(jumpValue.value);
}

function openItem(item) {
  saveItem(item);
  router.push(`/item/${item.id}`);
}

watch(() => [route.query.q, route.query.page], load, { immediate: true });
</script>
