<template>
  <div class="login-wrap">
    <section class="login-card">
      <div class="mascot">🐻</div>
      <h1>把钥匙放进糖罐</h1>
      <p class="meta">甜熊不扫码。把你自己浏览器里的闲鱼 Cookie 整段贴进来即可进店。</p>
      <textarea v-model="cookie" placeholder="t=...; cookie2=...; _m_h5_tk=..." />
      <p v-if="error" class="error">{{ error }}</p>
      <div style="margin-top: 16px; display: flex; gap: 10px">
        <button class="btn" :disabled="loading" @click="submit">打开店门</button>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useRoute, useRouter } from "vue-router";
import { login } from "../api";
import { setCookie } from "../session";

const cookie = ref("");
const error = ref("");
const loading = ref(false);
const router = useRouter();
const route = useRoute();

async function submit() {
  error.value = "";
  loading.value = true;
  try {
    await login(cookie.value.trim());
    setCookie(cookie.value.trim());
    router.replace(route.query.redirect || "/");
  } catch (err) {
    error.value = err.message;
  } finally {
    loading.value = false;
  }
}
</script>
