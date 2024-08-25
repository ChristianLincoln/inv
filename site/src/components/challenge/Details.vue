<template>
<v-row>
  <v-col>
    <h2>
    Challenge at a Glance
    </h2>
    <div class="p2">
    Bonus prize: {{ challenge_bonus }}<br>
    Timing: {{ challenge_timing }}<br>
    Points (max): {{ challenge_points }}<br>
    Prize money: {{ challenge_prize }}<br>
    </div><br>
    <h2>
    Challenge Introduction
    </h2>
    <div class="p2">
      {{ challenge_details }}
    </div>
  </v-col>
  <v-col>
    <v-img :src="challenge_poster"></v-img>
  </v-col>
</v-row>
</template>
<script>
function getPosterURL() {
  return new URL(challenge_poster, import.meta.url)
}
export default {
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
      
    }
  }
}
</script>