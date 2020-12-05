<template>
  <v-card id="card" elevation="10">
		<v-card-title>Upload Your Images</v-card-title>
		<v-card-text>File shoud be Jpeg, Png...</v-card-text>
    <form @submit.prevent>
      <div id="dropArea"
        @dragover.prevent
        @drop.prevent="onDragFile">
        <img src="../assets/image.svg" alt="" srcset="">
        <v-card-text>Drag & Drop Your Image Here</v-card-text>
      </div>
      <v-card-text>Or</v-card-text>

      <v-btn large color="primary" @click="onClickChooseBtn">Choose a file</v-btn>
      <input type="file" name="selectedFile" id="selectedFile" @change.prevent="onUploadFile" style="display:none;">
    </form>
  </v-card>
</template>

<script>
export default {
  data() {
    return {
      selectedFile: null,
    }
  },
  methods: {
    onDragFile(e) {
      this.selectedFile = e.dataTransfer.files[0];
      console.log(this.selectedFile);
    },
    onUploadFile(e) {
      this.selectedFile = e.target.files[0];
      console.log(this.selectedFile);
    },
    onClickChooseBtn() {
      document.querySelector('#selectedFile').click();
    }
  },

}
</script>

<style scoped>
  #card {
    position: relative;
    width: 360px;
    height: 440px;
    margin: 50px auto;
  }

  #card * {
    text-align: center !important;
    justify-content: center !important;
  }

  #dropArea {
    width: 85%;
    height: 60%;
    background: rgba(135, 207, 235, 0.1);
    border: 1px dashed skyblue;
    border-radius: 16px;
    margin: 0 auto;
  }

  img {
    margin-top: 10%;
  }

</style>