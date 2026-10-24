<template>
  <AppShell>
    <section class="panel">
      <div class="page-head">
        <h1>今日城堡橱窗</h1>
        <p class="meta">从闲鱼取来的新鲜闲置，点一下就能去找同类宝贝。</p>
      </div>
      <div class="chips">
        <button v-for="chip in chips" :key="chip" class="chip" @click="openSearch(chip)">
          {{ chip }}
        </button>
      </div>
    </section>

    <section class="shelf">
      <div class="shelf-head">
        <h2>新到货架</h2>
        <router-link to="/search?q=数码">查看全部</router-link>
      </div>
      <p v-if="error" class="error">{{ error }}</p>
      <div v-else class="grid">
        <CandyCard
          v-for="(item, index) in items"
          :key="item.id"
          :item="item"
          :priority="index < 10"
          @open="openItem"
        />
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
import { getCookie, saveItem, saveLastSearch } from "../session";

const router = useRouter();
const items = ref([]);
const error = ref("");
const chips = ["相机", "球鞋", "PS5光盘", "手机", "书桌", "自行车"];

function openSearch(q) {
  router.push({ path: "/search", query: { q } });
}

function openItem(item) {
  saveLastSearch("数码");
  saveItem(item);
  router.push(`/item/${item.id}`);
}

onMounted(async () => {
  try {
    const result = await searchItems(getCookie(), "数码", 1);
    items.value = result.items.slice(0, 10);
  } catch (err) {
    error.value = err.message;
  }
});
</script>
