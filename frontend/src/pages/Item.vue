<template>
  <AppShell>
    <PageBack />
    <article v-if="item" class="item-page">
      <div class="item-cover">
        <img
          v-if="item.picUrl"
          :src="cover"
          :alt="item.title"
          decoding="async"
          fetchpriority="high"
          referrerpolicy="no-referrer"
          @error="cover = item.picUrl"
        />
        <div v-else class="ph">无图</div>
      </div>
      <div class="item-info">
        <p class="meta">{{ item.area || "未知地区" }}</p>
        <h1>{{ item.title }}</h1>
        <div class="price">¥ {{ item.price }}</div>
        <p v-if="notice" class="notice">
          {{ notice.text }}
          <router-link :to="notice.to">{{ notice.link }}</router-link>
        </p>
        <div class="item-actions">
          <button class="btn" @click="want"><Icon name="heart" />我想要</button>
          <button class="btn ghost" @click="bag"><Icon name="bag" />加入订单</button>
        </div>
      </div>
    </article>
    <div v-else>
      <p class="error">找不到这件商品，请从列表重新点开。</p>
      <PageBack to="/search" label="返回搜索" />
    </div>
  </AppShell>
</template>

<script setup>
import { computed, ref, watch } from "vue";
import { useRoute } from "vue-router";
import AppShell from "../layouts/AppShell.vue";
import PageBack from "../components/PageBack.vue";
import Icon from "../components/Icon.vue";
import { thumbUrl } from "../image";
import { loadItem, loadList, saveList } from "../session";

const route = useRoute();
const notice = ref(null);
const item = computed(() => {
  const saved = loadItem();
  if (saved && String(saved.id) === String(route.params.id)) return saved;
  return null;
});
const cover = ref("");
watch(
  item,
  (value) => {
    cover.value = value?.picUrl ? thumbUrl(value.picUrl, 800) : "";
  },
  { immediate: true },
);

function shortTitle(title) {
  const text = title || "商品";
  return text.length > 28 ? text.slice(0, 28) + "…" : text;
}

function want() {
  if (!item.value) return;
  const messages = loadList("tianxiong.messages", []);
  messages.unshift({
    id: Date.now(),
    itemId: item.value.id,
    title: shortTitle(item.value.title),
    body: "已发送我想要",
  });
  saveList("tianxiong.messages", messages);
  notice.value = { text: "已记下，还在这件商品上。", link: "去看消息", to: "/messages" };
}

function bag() {
  if (!item.value) return;
  const orders = loadList("tianxiong.orders", []);
  orders.unshift({
    id: Date.now(),
    itemId: item.value.id,
    title: shortTitle(item.value.title),
    price: item.value.price,
    status: "待确认",
  });
  saveList("tianxiong.orders", orders);
  notice.value = { text: "已加入本地订单。", link: "去看订单", to: "/orders" };
}
</script>
