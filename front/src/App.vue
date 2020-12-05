<template>
  <v-app>
    <v-main>
      <v-container>
        <v-row justify="center">
          <v-col justify="center">
            <Uploader/>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>

import Uploader from './components/Uploader.vue';

export default {
  name: 'App',

  components: {
    Uploader,
  },

  data: () => ({
    //
  }),
};
</script>
