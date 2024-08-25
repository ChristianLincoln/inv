<script setup>
import Details from './challenge/Details.vue'
import Entry from './challenge/Entry.vue'
import Chatbot from './challenge/Chatbot.vue'
import Feedback from './challenge/Feedback.vue'
import Results from './challenge/Results.vue'
</script>
<template>
  <v-container class="d-flex flex-column ga-3">
    <v-card class="pa-7">
      <h2>
        <i>{{ prize_type }}</i>
      </h2>
      <h1>
        {{ challenge_title }}
      </h1>
    </v-card>
    <v-card variant="tonal">
      <v-card>
        <v-tabs
          v-model="tab"
          align-tabs="center"
          variant="flat"
        >
          <v-tab :value="1">Details</v-tab>
          <v-tab :value="2">Entry</v-tab>
          <v-tab :value="4">Feedback</v-tab>
          <v-tab :value="5">Chatbot</v-tab>
          <v-tab :value="3" disabled>Results</v-tab>
        </v-tabs>
      </v-card>
      <v-card-text>
        <v-tabs-window v-model="tab">
          <v-tabs-window-item :value="1">
            <Details
            :challenge_bonus="challenge_bonus"
            :challenge_timing="challenge_timing"
            :challenge_points="challenge_points"
            :challenge_prize="challenge_prize"
            :challenge_details="challenge_details"
            :challenge_poster="challenge_poster"
            ></Details>
          </v-tabs-window-item>
          <v-tabs-window-item :value="2">
            <Entry/>
          </v-tabs-window-item>
          <v-tabs-window-item :value="3">
            <Results/>
          </v-tabs-window-item>
          <v-tabs-window-item :value="4">
            <Feedback/>
          </v-tabs-window-item>
          <v-tabs-window-item :value="5">
            <Chatbot speaker="Jaimes and Mairk"/>
          </v-tabs-window-item>
        </v-tabs-window>
      </v-card-text>
    </v-card>
  </v-container>
</template>
<script>
export default {
  name: 'challenge',
  props:[
    "prize_type",
    "challenge_title",
    "challenge_timing",
    "challenge_bonus",
    "challenge_prize",
    "challenge_details",
    "challenge_points",
    "challenge_poster",],
  data() {
    return {
      tab: null,
    }
  }
}
</script>