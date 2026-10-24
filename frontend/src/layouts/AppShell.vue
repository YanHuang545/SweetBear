<template>
  <div class="shell">
    <aside class="rail">
      <router-link
        to="/"
        class="logo"
        :class="{ waving }"
        @mouseenter="wave"
      >
        <div class="logo-mark">
          <img src="/logo-mark.jpg?v=1" alt="雪莉玫" />
        </div>
        <div>
          <div class="brand">甜熊</div>
          <p class="logo-sub">梦幻闲置集市</p>
        </div>
        <p class="logo-bubble">{{ hello }}</p>
      </router-link>
      <nav>
        <router-link to="/" data-hi="回城堡啦">
          <Icon name="home" />
          <span>首页</span>
        </router-link>
        <router-link to="/search" data-hi="去找宝贝">
          <Icon name="search" />
          <span>搜索</span>
        </router-link>
        <router-link to="/publish" data-hi="摆个小摊">
          <Icon name="publish" />
          <span>发布</span>
        </router-link>
        <router-link to="/messages" data-hi="有人找你玩">
          <Icon name="messages" />
          <span>消息</span>
        </router-link>
        <router-link to="/orders" data-hi="看看小包裹">
          <Icon name="orders" />
          <span>订单</span>
        </router-link>
        <router-link to="/me" data-hi="城堡主人">
          <Icon name="me" />
          <span>我的</span>
        </router-link>
      </nav>
    </aside>
    <main class="stage">
      <div class="stage-bg" aria-hidden="true"></div>
      <div class="stage-content">
        <form class="topbar" @submit.prevent="goSearch">
          <div class="search-box">
            <div class="search-pill">
              <Icon name="search" />
              <input v-model="keyword" placeholder="在城堡里找一件闲置…" />
              <button type="submit">搜索</button>
            </div>
            <p class="search-hi">说出想找的宝贝，城堡帮你找～</p>
          </div>
        </form>
        <slot />
      </div>
    </main>
  </div>
</template>

<script setup>
import { onMounted, ref } from "vue";
import { useRouter } from "vue-router";
import Icon from "../components/Icon.vue";

const HELLOS = [
  "欢迎来甜熊的城堡购物哦",
  "今天想带哪件宝贝回家呀？",
  "摸摸头～慢慢逛就好啦",
];

const router = useRouter();
const keyword = ref("");
const hello = ref(HELLOS[0]);
const waving = ref(true);

function wave() {
  hello.value = HELLOS[Math.floor(Math.random() * HELLOS.length)];
}

function goSearch() {
  const q = keyword.value.trim();
  if (!q) return;
  router.push({ path: "/search", query: { q } });
}

onMounted(() => {
  window.setTimeout(() => {
    waving.value = false;
  }, 2800);
});
</script>
