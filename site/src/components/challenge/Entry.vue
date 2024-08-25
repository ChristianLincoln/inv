<template>
<v-expansion-panels>
  <v-card-text>
    <h2>Step 1</h2>
    <p>Interact with the chatbot (right) to learn about the challenges Inversity faces. Try prompts like 'Hi what's your name and what do you do?' to get started.</p>
    <h2>Step 2</h2>
    <p>Build a prototype of a product you believe could solve one of the problems detailed. We do not expect an all-singing-all-dancing product - we expect a prototype which you've spent a few hours building.</p>
    <h2>Step 3</h2>
    <p>Enter the link to your code repo below - make sure the repo is made public so we can view it.</p>
    <h2>Step 4</h2>
    <p>Submit a 3-minute video pitch about your product to Inversity below.</p>
  </v-card-text>
  <v-expansion-panel>
    <v-expansion-panel-title disable-icon-rotate>
      Title
      <template v-slot:actions>
        <v-icon icon="mdi-checkbox-blank-outline"> </v-icon>
      </template>
    </v-expansion-panel-title>
  </v-expansion-panel>
  <v-expansion-panel>
    <v-expansion-panel-title disable-icon-rotate>
      Github
      <template v-slot:actions>
        <v-icon icon="mdi-checkbox-blank-outline"> </v-icon>
      </template>
    </v-expansion-panel-title>
  </v-expansion-panel>
  <v-expansion-panel>
    <v-expansion-panel-title disable-icon-rotate>
      Pitch
      <template v-slot:actions>
        <v-icon icon="mdi-checkbox-blank-outline"> </v-icon>
      </template>
    </v-expansion-panel-title>
  </v-expansion-panel>
</v-expansion-panels>
</template>
<script>
export default {
  data() {
    return {
    }
  }
}
</script>