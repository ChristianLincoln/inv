<template>
<v-virtual-scroll :items="chat" :height="400">
  <template v-slot:default="{ item }">
    <Message :title="item.title" :avatar="item.avatar" :content="item.content"></Message>
  </template>
</v-virtual-scroll class="mb-4">
<v-text-field label="Message" @click:append="sendMessage" append-icon="mdi-send" clearable v-model="messageField">
</v-text-field>
<v-file-input v-model="fileInput" label="File Attachment" clearable></v-file-input>
</template>
<script>
import {inject} from 'vue'
import Message from './Message.vue'
import ChatbotProfile from '@/assets/chatbot.webp'
export default {
  setup() {
    const UserAvatar = inject('user-avatar')
    const UserName = inject('user-name')
    console.log(UserName)
    return {UserName,UserAvatar,ChatbotProfile}
  },
  components: {
    'Message': Message
  },
  props: ["speaker"],
  data() {
    return {
      messageField: null,
      fileInput: null,
      chat: [
        {content:"Send a message to gather crucial market research and receive feedback!",title:"Chatbot Interview"}
      ],
      messages: [
      ]
    }
  },
  methods: {
    sendMessage: function(message) {
      const send = ({file_name,file_data}) => {
        this.chat.push({content:this.messageField,avatar:this.UserAvatar,title:this.UserName});
        let message = this.messageField;
        if (file_data) {
          message+="\nattachment:"+file_data;
          this.chat.push({content:file_name,avatar:this.UserAvatar,title:this.UserName});
        }
        this.messages.push({role:"user",content:message})
        fetch("/api/chatbot",{method:"POST",body: JSON.stringify(this.messages)}).then((response) => {
          response.text().then((result)=>{
            if (response.ok) {
              this.messageField = "";
              this.fileInput = null;
              this.messages.push({role:"system",content:result})
              this.chat.push({content:result,title:this.speaker,avatar:ChatbotProfile})
            } else {
              this.chat.push({content:"Sorry. There was an error requesting a response."})
            }
          })
        });
      }
      if (this.fileInput) {
        this.fileInput.text().then((data) => {
          send({file_data:data,file_name:this.fileInput.name});
        });
      } else {
        send({file_data:null,file_name:null});
      }
    }
  }
}
</script>