<template>
<v-infinite-scroll :height="400" mode="manual" @load="loadPosts" :items="posts" class="mb-4">
  <div>
    <template v-for="item in posts">
      <Post :title="item.title" :avatar="item.avatar" :content="item.content" :no_replies="item.no_replies" :id="item.id" :file="item.file" :file_name="item.file_name"></Post>
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
<v-textarea label="Post" v-model="messageField" ></v-textarea>
<v-file-input v-model="fileInput" label="File Attachment" @click:append="sendPost" append-icon="mdi-send" clearable></v-file-input>
</template>
<script>
import {inject} from 'vue'
import Message from './Message.vue'
import Post from './Post.vue'
export default {
  setup() {
    const userAvatar = inject('user-avatar')
    const userName = inject('user-name')
    const userId = inject('user-id')
    return {userId,userName,userAvatar}
  },
  components: {
    'Post': Post,
    'Message': Message
  },
  methods: {
    sendPost: function() {
      const send = ({file_id,file_name}) => {
        let url = "/api/makepost"
        if (file_id) {url+="/"+file_id}
        fetch(url,{body:this.messageField,headers:{authentication:this.userId},method:"POST"}).then((response) => {
          if (response.ok) {
            this.messageField = ""
            this.fileInput = null
            this.loadPosts({done:()=>{}});
          }
        })
      }
      if (this.fileInput) {
        this.fileInput.text().then((data) => {
          fetch("/api/makefile/"+this.fileInput.name,{body:data,method:"POST"}).then((response) => {
            if (response.ok) {
              response.text().then((id) => {
                send({file_id:id,file_name:this.fileInput.name});
              })
            }
          })
        });
      } else {
        send({file_id:null,file_name:null});
      }
    },
    loadPosts: function({done}) {
      fetch("/api/getposts").then((response) => {
        if (response.ok) {
          let results = response.json().then((posts) => {
            this.posts = [this.posts[0]]
            posts.forEach((post) => {
              console.log(post)
              if (post.file.length > 0) {post.file = "/api/getfile/"+post.file+"/"+post.file_name} else {post.file = null}
              this.posts.push(post)
            })
          })
          done("ok")
        } else {
          done("error")
        }
      })
    }
  },
  data() {
    return {
      page: 1,
      posts: [{content:"Send a post to collaborate and get live feedback from the challenge hosts themselves!",title:"Feedback Forum",no_replies:true}],
      fileInput: null,
      messageField: null,
    }
  },
  watch: {
    "page": (page) => {
        console.log(page)
    }
  },
  mounted() {
    this.loadPosts({done:()=>{}});
  }
}
</script>