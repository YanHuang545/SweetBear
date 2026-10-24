<template>
  <div class="login-wrap">
    <section class="login-card">
      <div class="login-bear" :class="{ waving }" @mouseenter="wave">
        <div class="logo-mark">
          <img src="/logo-mark.jpg?v=1" alt="雪莉玫" />
        </div>
        <p class="logo-bubble">{{ hello }}</p>
      </div>
      <p class="login-kicker">ONCE UPON A BEAR</p>
      <h1>欢迎来到甜熊城堡</h1>
      <p class="meta">
        不扫码。在 www.goofish.com 保持登录后，从 DevTools → Application → Cookies
        复制整段粘贴。需要包含 cookie2、_m_h5_tk、_m_h5_tk_enc。
      </p>
      <label class="field-label">Cookie</label>
      <textarea v-model="cookie" placeholder="t=...; cookie2=...; _m_h5_tk=..." />
      <p v-if="error" class="error">{{ error }}</p>
      <div style="margin-top: 16px">
        <button class="btn" :disabled="loading" @click="submit">
          {{ loading ? "开门中…" : "推开城堡门" }}
        </button>
      </div>
    </section>
  </div>
</template>

<script setup>
import { onMounted, ref } from "vue";
import { useRoute, useRouter } from "vue-router";
import { login } from "../api";
import { setCookie } from "../session";

const HELLOS = [
  "欢迎来甜熊的城堡购物哦",
  "把钥匙给我，我帮你开门～",
  "摸摸头，先进来坐坐吧",
];

const router = useRouter();
const route = useRoute();
const cookie = ref("");
const hello = ref(HELLOS[0]);
const waving = ref(true);

function wave() {
  hello.value = HELLOS[Math.floor(Math.random() * HELLOS.length)];
}
const error = ref(typeof route.query.reason === "string" ? route.query.reason : "");
const loading = ref(false);

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

onMounted(() => {
  window.setTimeout(() => {
    waving.value = false;
  }, 2800);
});
</script>
