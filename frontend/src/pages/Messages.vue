<template>
  <AppShell>
    <PageBack />
    <div class="page-head">
      <h1>消息</h1>
      <p class="meta">这里是本机询价记录，点一条可回到对应商品。</p>
    </div>
    <div v-if="messages.length" class="list">
      <article
        v-for="msg in messages"
        :key="msg.id"
        class="list-item"
        :class="{ clickable: msg.itemId }"
        @click="openItem(msg)"
      >
        <div>
          <strong>{{ msg.title }}</strong>
          <p class="meta">{{ msg.body }}</p>
        </div>
      </article>
    </div>
    <div v-else class="empty">
      还没有消息。
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
const messages = ref(loadList("tianxiong.messages", []));

function openItem(msg) {
  const found = loadItemById(msg.itemId);
  if (!found) return;
  saveItem(found);
  router.push(`/item/${found.id}`);
}
</script>
