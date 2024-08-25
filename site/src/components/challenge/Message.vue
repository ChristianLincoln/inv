<template>
<v-card
  :prepend-avatar="avatar"
  :title="name"
  class="mb-4"
>
  <v-card-text>
    {{ content }}
  </v-card-text>
</v-card>
</template>
<script>
export default {
  props:["name","content","avatar"],
  data() {
    return {
    }
  }
}
</script>