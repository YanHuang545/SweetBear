<template>
  <AppShell>
    <PageBack />
    <section class="panel profile-card">
      <div class="page-head">
        <h1>我的</h1>
        <p class="meta">在这里退出后需要重新粘贴 Cookie 才能搜索。</p>
      </div>
      <button class="btn ghost" @click="logout">退出登录</button>
    </section>
  </AppShell>
</template>

<script setup>
import { useRouter } from "vue-router";
import AppShell from "../layouts/AppShell.vue";
import PageBack from "../components/PageBack.vue";
import { clearCookie } from "../session";

const router = useRouter();

function logout() {
  clearCookie();
  router.replace("/login");
}
</script>
