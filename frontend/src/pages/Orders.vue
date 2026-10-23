<template>
  <AppShell>
    <h1>口袋里的糖</h1>
    <p class="meta">订单先存在本机，不当成闲鱼真实成交。</p>
    <article v-for="order in orders" :key="order.id" class="panel" style="margin-top: 12px">
      <div class="price">¥ {{ order.price }}</div>
      <p>{{ order.title }}</p>
      <div class="meta">{{ order.status }}</div>
    </article>
    <p v-if="!orders.length" class="empty">口袋还空着。</p>
  </AppShell>
</template>

<script setup>
import { ref } from "vue";
import AppShell from "../layouts/AppShell.vue";
import { loadList } from "../session";

const orders = ref(loadList("tianxiong.orders", []));
</script>
