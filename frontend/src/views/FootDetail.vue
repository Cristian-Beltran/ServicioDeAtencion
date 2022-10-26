<template>
  <div class="relative py-16 overflow-hidden">
    <div class="relative px-4 sm:px-6 lg:px-8">
      <div class="text-lg max-w-prose mx-auto">
        <h1>
          <span
            class="mt-2 block text-3xl text-center leading-8 font-extrabold tracking-tight text-gray-900 sm:text-4xl"
            >{{ APIData.name }}</span
          >
        </h1>
        <p class="mt-8 text-xl text-gray-500 leading-8"></p>
      </div>
      <div class="mt-6 prose prose-indigo prose-lg text-gray-500 mx-auto">
        {{ APIData.description }}
      </div>
    </div>
  </div>
</template>
<script>
import { getAPI } from "../axios-api";
export default {
  name: "FootDetail",
  data() {
    return {
      APIData: {},
    };
  },
  created() {
    let id = this.$route.params.id;
    getAPI
      .get("/foot/foot/" + id)
      .then((response) => {
        this.APIData = response.data;
      })
      .catch((err) => {
        console.log(err);
      });
  },
};
</script>
