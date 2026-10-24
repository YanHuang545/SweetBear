<template>
  <AppShell>
    <PageBack />
    <section class="panel" style="max-width: 640px">
      <div class="page-head">
        <h1>发布闲置</h1>
        <p class="meta">只保存在本机浏览器，不会发到闲鱼。</p>
      </div>
      <label class="field-label">标题</label>
      <input v-model="title" class="field" />
      <label class="field-label">价格</label>
      <input v-model="price" class="field" />
      <label class="field-label">说明</label>
      <textarea v-model="story" />
      <button class="btn" style="margin-top: 16px" @click="save">
        <Icon name="publish" />保存草稿
      </button>
    </section>
    <section class="shelf">
      <div class="shelf-head">
        <h2>本地草稿</h2>
      </div>
      <div v-if="drafts.length" class="grid">
        <article v-for="draft in drafts" :key="draft.id" class="goods">
          <div class="goods-cover">
            <div class="ph">草稿</div>
          </div>
          <div class="goods-body">
            <p class="goods-title">{{ draft.title }}</p>
            <div class="goods-foot">
              <span class="price">¥ {{ draft.price }}</span>
            </div>
          </div>
        </article>
      </div>
      <p v-else class="empty">还没有草稿。</p>
    </section>
  </AppShell>
</template>

<script setup>
import { ref } from "vue";
import AppShell from "../layouts/AppShell.vue";
import PageBack from "../components/PageBack.vue";
import Icon from "../components/Icon.vue";
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
