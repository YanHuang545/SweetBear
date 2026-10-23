<template>
  <AppShell>
    <section class="panel">
      <h1>今日糖纸</h1>
      <p class="meta">横着逛，不像闲鱼那样一排排往下掉。</p>
      <div class="chips" style="margin-top: 14px">
        <button v-for="chip in chips" :key="chip" class="chip" @click="openSearch(chip)">
          {{ chip }}
        </button>
      </div>
    </section>

    <section class="shelf">
      <div class="shelf-head">
        <h2>新鲜出炉</h2>
        <router-link class="meta" to="/search?q=数码">整条货架 →</router-link>
      </div>
      <p v-if="error" class="error">{{ error }}</p>
      <div v-else class="row">
        <CandyCard v-for="item in items" :key="item.id" :item="item" @open="openItem" />
      </div>
    </section>
  </AppShell>
</template>

<script setup>
import { onMounted, ref } from "vue";
import { useRouter } from "vue-router";
import AppShell from "../layouts/AppShell.vue";
import CandyCard from "../components/CandyCard.vue";
import { searchItems } from "../api";
import { getCookie, saveItem } from "../session";

const router = useRouter();
const items = ref([]);
const error = ref("");
const chips = ["相机", "球鞋", "PS5光盘", "手机", "书桌", "自行车"];

function openSearch(q) {
  router.push({ path: "/search", query: { q } });
}

function openItem(item) {
  saveItem(item);
  router.push(`/item/${item.id}`);
}

onMounted(async () => {
  try {
    const result = await searchItems(getCookie(), "数码", 1);
    items.value = result.items.slice(0, 12);
  } catch (err) {
    error.value = err.message;
  }
});
</script>
