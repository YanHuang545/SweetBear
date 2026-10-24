<template>
  <AppShell>
    <PageBack />
    <div class="page-head">
      <h1>订单</h1>
      <p class="meta">本机收藏的意向单，点一条可回到对应商品。</p>
    </div>
    <div v-if="orders.length" class="list">
      <article
        v-for="order in orders"
        :key="order.id"
        class="list-item"
        :class="{ clickable: order.itemId }"
        @click="openItem(order)"
      >
        <div>
          <p>{{ order.title }}</p>
          <div class="meta">{{ order.status }}</div>
        </div>
        <div class="price">¥ {{ order.price }}</div>
      </article>
    </div>
    <div v-else class="empty">
      还没有订单。
      <router-link to="/">去首页看看</router-link>
    </div>
  </AppShell>
</template>

<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";
import AppShell from "../layouts/AppShell.vue";
import PageBack from "../components/PageBack.vue";
import { loadItemById, loadList, saveItem } from "../session";

const router = useRouter();
const orders = ref(loadList("tianxiong.orders", []));

function openItem(order) {
  const found = loadItemById(order.itemId);
  if (!found) return;
  saveItem(found);
  router.push(`/item/${found.id}`);
}
</script>
