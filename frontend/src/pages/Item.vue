<template>
  <AppShell>
    <article v-if="item" class="panel" style="display: grid; grid-template-columns: 1.1fr 1fr; gap: 28px">
      <img v-if="item.picUrl" :src="item.picUrl" :alt="item.title" style="border-radius: 28px" />
      <div v-else class="ph" style="height: 320px; border-radius: 28px">🍬</div>
      <div>
        <p class="meta">{{ item.area }}</p>
        <h1>{{ item.title }}</h1>
        <div class="price">¥ {{ item.price }}</div>
        <p>这张糖纸来自寻宝货架。想聊价就去「纸条」，想收下就丢进「口袋」。</p>
        <div style="display: flex; gap: 10px; margin-top: 18px">
          <button class="btn" @click="want">我想要</button>
          <button class="btn mint" @click="bag">放进口袋</button>
        </div>
      </div>
    </article>
    <p v-else class="error">找不到这张糖纸，先回货架再点一次。</p>
  </AppShell>
</template>

<script setup>
import { computed } from "vue";
import { useRoute, useRouter } from "vue-router";
import AppShell from "../layouts/AppShell.vue";
import { loadItem, loadList, saveList } from "../session";

const route = useRoute();
const router = useRouter();
const item = computed(() => {
  const saved = loadItem();
  if (saved && String(saved.id) === String(route.params.id)) return saved;
  return null;
});

function want() {
  const messages = loadList("tianxiong.messages", []);
  messages.unshift({
    id: Date.now(),
    title: "我想要：" + (item.value?.title || ""),
    body: "已向糖纸对面丢了一张纸条（本地演示）。",
  });
  saveList("tianxiong.messages", messages);
  router.push("/messages");
}

function bag() {
  const orders = loadList("tianxiong.orders", []);
  orders.unshift({
    id: Date.now(),
    title: item.value?.title,
    price: item.value?.price,
    status: "待当面核糖",
  });
  saveList("tianxiong.orders", orders);
  router.push("/orders");
}
</script>
