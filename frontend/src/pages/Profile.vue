<template>
  <AppShell>
    <section class="panel">
      <div class="mascot">🐻</div>
      <h1>{{ nick }} 的熊窝</h1>
      <p class="meta">登录态来自你贴进来的 Cookie，不是扫码。</p>
      <button class="btn ghost" @click="logout">抽出钥匙离开</button>
    </section>
  </AppShell>
</template>

<script setup>
import { useRouter } from "vue-router";
import AppShell from "../layouts/AppShell.vue";
import { clearCookie, nickFromCookie } from "../session";

const router = useRouter();
const nick = nickFromCookie();

function logout() {
  clearCookie();
  router.replace("/login");
}
</script>
