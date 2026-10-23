<template>
  <div class="shell">
    <aside class="rail">
      <div class="mascot">🐻</div>
      <div class="brand" style="font-size: 28px">甜熊</div>
      <p class="meta" style="color: rgba(248, 239, 228, 0.7)">糖纸上的闲置集市</p>
      <nav>
        <router-link to="/">首页货架</router-link>
        <router-link to="/search">寻宝</router-link>
        <router-link to="/publish">放上糖纸</router-link>
        <router-link to="/messages">纸条</router-link>
        <router-link to="/orders">口袋</router-link>
        <router-link to="/me">我的熊窝</router-link>
      </nav>
    </aside>
    <main class="stage">
      <form class="topbar" @submit.prevent="goSearch">
        <div class="search-pill">
          <input v-model="keyword" placeholder="在糖罐里找一件闲置…" />
          <button type="submit">寻宝</button>
        </div>
        <span class="meta">{{ nick }}</span>
      </form>
      <slot />
    </main>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";
import { nickFromCookie } from "../session";

const router = useRouter();
const keyword = ref("");
const nick = nickFromCookie();

function goSearch() {
  const q = keyword.value.trim();
  if (!q) return;
  router.push({ path: "/search", query: { q } });
}
</script>
