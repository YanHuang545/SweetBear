<template>
  <AppShell>
    <section class="panel" style="max-width: 640px">
      <h1>放上一张新糖纸</h1>
      <p class="meta">发闲置先记在你的浏览器里，不经过闲鱼发布接口。</p>
      <label>标题</label>
      <input v-model="title" class="field" />
      <label style="display: block; margin-top: 12px">价格</label>
      <input v-model="price" class="field" />
      <label style="display: block; margin-top: 12px">故事</label>
      <textarea v-model="story" />
      <button class="btn" style="margin-top: 16px" @click="save">贴上糖罐</button>
    </section>
    <section class="shelf">
      <h2>已贴的糖纸</h2>
      <div v-if="drafts.length" class="grid">
        <article v-for="draft in drafts" :key="draft.id" class="candy">
          <div class="ph">📝</div>
          <div class="candy-body">
            <div class="price">¥ {{ draft.price }}</div>
            <p>{{ draft.title }}</p>
          </div>
        </article>
      </div>
      <p v-else class="meta">还没有草稿。</p>
    </section>
  </AppShell>
</template>

<script setup>
import { ref } from "vue";
import AppShell from "../layouts/AppShell.vue";
import { loadList, saveList } from "../session";

const title = ref("");
const price = ref("");
const story = ref("");
const drafts = ref(loadList("tianxiong.drafts", []));

function save() {
  if (!title.value.trim()) return;
  drafts.value.unshift({
    id: Date.now(),
    title: title.value.trim(),
    price: price.value.trim() || "0",
    story: story.value.trim(),
  });
  saveList("tianxiong.drafts", drafts.value);
  title.value = "";
  price.value = "";
  story.value = "";
}
</script>
