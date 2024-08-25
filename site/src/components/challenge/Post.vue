<template>
<v-card
  :prepend-avatar="avatar"
  :title="name"
  class="mb-4"
>
  <v-card-text>
    {{ content }}
  </v-card-text>
  <v-card-actions v-if="file">
    <v-btn :href="file" download>
      {{ file_name }}
    </v-btn>
  </v-card-actions>
  <v-expansion-panels v-if="!no_replies">
    <v-expansion-panel title="Replies" @click="onExpanded">
      <v-expansion-panel-text>
        <v-infinite-scroll mode="manual" @load="loadMessages" :items="messages" class="mb-4">
          <div>
            <template v-for="item in messages">
              <Message :title="item.title" :avatar="item.avatar" :content="item.content"></Message>
            </template>
          </div>
          <template v-slot:load-more="{ props }">
            <v-btn
              icon="mdi-refresh"
              size="small"
              variant="text"
              v-bind="props"
            ></v-btn>
          </template>
          <template v-slot:error="{ props }">
            <v-alert type="error">
              <div class="d-flex justify-space-between align-center">
                Something went wrong...
                <v-btn color="white" size="small" variant="outlined" v-bind="props">
                  Retry
                </v-btn>
              </div>
            </v-alert>
          </template>
        </v-infinite-scroll>
        <v-text-field label="Reply" @click:append="sendMessage" append-icon="mdi-send" clearable v-model="messageField"></v-text-field>
      </v-expansion-panel-text>
    </v-expansion-panel>
  </v-expansion-panels>
</v-card>
</template>
<script>
import {inject} from 'vue'
export default {
  props:["name","content","avatar","no_replies","id","file","file_name"],
  setup() {
    const userId = inject('user-id')
    return {userId}
  },
  data() {
    return {
      messageField: null,
      messages: []
    }
  },
  methods: {
    sendMessage() {
      fetch("/api/makemessage/"+this.id,{body:this.messageField,headers:{authentication:this.userId},method:"POST"}).then((response) => {
        if (response.ok) {
          this.messageField = ""
          this.loadMessages({done:()=>{}});
        }
      })
    },
    onExpanded() {
      this.loadMessages({done:()=>{}});
    },
    loadMessages({done}) {
      fetch("/api/getmessages/"+this.id).then((response) => {
        if (response.ok) {
          let results = response.json().then((messages) => {
            this.messages = []
            messages.forEach((message) => {
              console.log(message)
              this.messages.push(message)
            })
          })
          done("ok")
        } else {
          done("error")
        }
      })
    }
  }
}
</script>