<template>
  <AppShell>
    <h1>纸条盒</h1>
    <p class="meta">闲鱼消息接口还没接到甜熊，这里只留本地纸条。</p>
    <article v-for="msg in messages" :key="msg.id" class="panel" style="margin-top: 12px">
      <strong>{{ msg.title }}</strong>
      <p>{{ msg.body }}</p>
    </article>
    <p v-if="!messages.length" class="empty">盒子是空的。去商品页点「我想要」会落下第一张。</p>
  </AppShell>
</template>

<script setup>
import { ref } from "vue";
import AppShell from "../layouts/AppShell.vue";
import { loadList } from "../session";

const messages = ref(loadList("tianxiong.messages", []));
</script>
