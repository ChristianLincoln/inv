<template>
  <v-app>
    <v-app-bar app dark collapse-on-scroll>
      <v-app-bar-nav-icon @click.stop="drawer = !drawer"> </v-app-bar-nav-icon>
      <v-img height="40" src='@/assets/logo.svg' />
      <v-btn>Logout</v-btn>
    </v-app-bar>
    <v-navigation-drawer v-model="drawer" temporary>
      <v-list>
        <v-list-item
            :prepend-avatar="userAvatar"
            subtitle="Organisation"
            :title="userName"
        ></v-list-item>
      </v-list>
      <v-list>
        <v-list-item title="Account" prepend-icon="mdi-account-multiple" @click="user_selector = !user_selector"></v-list-item>
        <v-list-item title="Challenges" prepend-icon="mdi-star"></v-list-item>
        <v-list-item title="Settings" prepend-icon="mdi-cog" @click="theme_selector = !theme_selector"></v-list-item>
        <v-list-item title="Learning" prepend-icon="mdi-book"></v-list-item>
        <v-list-item title="History" prepend-icon="mdi-account-multiple"></v-list-item>
      </v-list>
    </v-navigation-drawer>
    <v-main>
      <challenge 
        prize_type = "Individual Prize"
        challenge_title = "‘Learner Takeover 1.0: Boosting personalisation, community and realism on Inversity’"
        tab = null
        challenge_timing = "2 Aug 2024 - 25 Aug 2024"
        challenge_bonus = "N/A"
        challenge_prize = "N/A"
        challenge_details = "We're handing the keys over to you! In this challenge, you get the chance to build the future features on Inversity. First, chat to the challenge chatbot - trained on a conversation with James & Mark - and understand their vision for Inversity. Combine this with your own experiences of the platform to come up with creative new features which help make Inversity more personalised, have a greater sense of community, and increase the realism of the challenges. This challenge is open to all Inversity learners - including those without a subscription! The winner will get the unique opportunity for a 2-day internship (all expenses paid) with Mark & James to take their prototype to the next level!"
        challenge_points = "domain 60, problem_solving 6, communication 6"
        :challenge_poster = "ChallengePoster"
      ></challenge>
    </v-main>
    <v-bottom-sheet v-model="user_selector">
      <v-card
        title="Select User"
      >
        <v-card-text>
          <v-text-field label="User Id" @click:append="loadUser" append-icon="mdi-reload-alert" v-model="userId"></v-text-field>
        </v-card-text>
      </v-card>
    </v-bottom-sheet>
    <v-bottom-sheet v-model="theme_selector">
      <v-card>
        <v-card-text>
          <v-select
            label="Select Theme"
            v-model="selectedTheme"
            :items="themes"
            @update:modelValue="this.setTheme()"
          ></v-select>
        </v-card-text>
      </v-card>
    </v-bottom-sheet>
  </v-app>
</template>
<script>
/* This is my Inversity replica that is used to demonstrate some of the proposals in my pitch:
- A bit of theming and personalisation with vuetify?
- Using a drawer as a menu and mixing up the UI a bit.
- Adding the Feedback and Chatbot tabs in the challenge.

I have used literal data in this Vue as this is static and for demonstration purposes, later components will use some props.
*/
import Challenge from './components/Challenge.vue'
import ChallengePoster from '@/assets/challengeposter.webp'
import UserProfile from '@/assets/me.jpg'
import {provide,ref} from 'vue'
import {useTheme} from "vuetify";
export default {
  setup() {
    const theme = useTheme();
    const myThemes = ["inversityTheme","nightTheme","oceanTheme"];
    const selectedTheme = ref(myThemes[0]);
    
    const setTheme = () => {
      theme.global.name.value = selectedTheme.value;
      console.log(selectedTheme.value);
    };

    const userAvatar = ref("https://cdn.vuetifyjs.com/images/john.jpg")
    const userName = ref("John Leider")
    const userId = ref(3)
    provide('user-avatar',userAvatar)
    provide('user-name',userName)
    provide('user-id',userId)

    return {userName,userAvatar,userId,ChallengePoster,setTheme,selectedTheme}
  },
  components: {
    'Challenge': Challenge
  },
  name: 'app',
  data() {
    return {
      components: {
        'challenge': Challenge
      },
      themes:["inversityTheme","nightTheme","oceanTheme"],
      user_selector: null,
      theme_selector: null,
      drawer: false,
      tab: null,
      watch: {
        group() {
          this.drawer = true;
        },
      },
    }
  },
  methods: {
    loadUser() {
      fetch("/api/getuser/"+this.userId).then((response) => {
        if (response.ok) {
          response.json().then((details) => {
            this.userName = details.name;
            this.userAvatar = details.avatar;
          })
        } else {
          console.log("Could not find user!");
        }
      });
    }
  },
  mounted() {
    this.loadUser();
  }
}
</script>