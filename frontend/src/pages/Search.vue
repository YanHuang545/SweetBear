<template>
  <AppShell>
    <h1>寻宝：{{ keyword || "随便看看" }}</h1>
    <p v-if="error" class="error">{{ error }}</p>
    <p v-else-if="loading" class="meta">糖纸正在展开…</p>
    <div v-else class="grid">
      <CandyCard v-for="item in items" :key="item.id" :item="item" @open="openItem" />
    </div>
    <div class="pager">
      <button class="btn ghost" :disabled="page <= 1 || loading" @click="turn(-1)">上一卷</button>
      <span>第 {{ page }} 页</span>
      <button class="btn ghost" :disabled="loading || items.length < 1" @click="turn(1)">下一卷</button>
    </div>
  </AppShell>
</template>

<script setup>
import { ref, watch } from "vue";
import { useRoute, useRouter } from "vue-router";
import AppShell from "../layouts/AppShell.vue";
import CandyCard from "../components/CandyCard.vue";
import { searchItems } from "../api";
import { getCookie, saveItem } from "../session";

const route = useRoute();
const router = useRouter();
const items = ref([]);
const error = ref("");
const loading = ref(false);
const page = ref(1);
const keyword = ref("");

async function load() {
  keyword.value = String(route.query.q || "数码");
  page.value = Number(route.query.page || 1);
  loading.value = true;
  error.value = "";
  try {
    const result = await searchItems(getCookie(), keyword.value, page.value);
    items.value = result.items;
    if (!result.items.length) error.value = "这页糖纸是空的";
  } catch (err) {
    error.value = err.message;
    items.value = [];
  } finally {
    loading.value = false;
  }
}

function turn(delta) {
  const next = Math.max(1, page.value + delta);
  router.push({ path: "/search", query: { q: keyword.value, page: String(next) } });
}

function openItem(item) {
  saveItem(item);
  router.push(`/item/${item.id}`);
}

watch(() => [route.query.q, route.query.page], load, { immediate: true });
</script>
