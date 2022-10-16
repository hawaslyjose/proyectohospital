<template>
  <div class="post_psalud">
    <div class="container_PostPsalud">
      <h2>Registro Personal Salud</h2>
      <form v-on:submit.prevent="processPostPsalud">
        <input type="text" placeholder="Username" v-model="medico.usuario" />
        <br />
        <input type="text" placeholder="Rol" v-model="medico.rol" />
        <br />
        <input
          type="text"
          placeholder="Especialidad"
          v-model="medico.especialidad"
        />
        <input type="text" placeholder="licencia" v-model="medico.licencia" />
        <br />
        <br />
        <button type="submit">Registrar</button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "Postpsalud",
  data: function () {
    return {
      medico: {
        usuario: "",
        rol: "",
        especialidad: "",
        licencia: "",
      },
    };
  },
  methods: {
    processPostPsalud: function () {
      axios
        .post("http://127.0.0.1:8000/personalsaludCrear/", this.medico, {
          headers: {},
        })
        .then((result) => {
          alert("Personal salud registrado");
        })
        .catch((error) => {
          console.log(error);
          alert("error de registro");
        });
    },
  },
};
</script>

<style>
.post_psalud {
  margin: 0;
  padding: 0%;
  height: 100%;
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.container_PostPsalud {
  border: 3px solid #283747;
  border-radius: 10px;
  width: 35%;
  height: 95%;
  background: #e5e7e9;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.post_psalud h2 {
  color: #283747;
}

.post_psalud form {
  width: 70%;
}

.post_psalud input {
  height: 40px;
  width: 100%;
  box-sizing: border-box;
  padding: 10px 20px;
  margin: 5px 0;
  border: 1px solid #283747;
}

.post_psalud button {
  width: 100%;
  height: 40px;
  color: #e5e7e9;
  background: #283747;
  border: 1px solid #e5e7e9;
  border-radius: 5px;
  padding: 10px 25px;
  margin: 5px 0 25px 0;
}

.post_psalud button:hover {
  color: #e5e7e9;
  background: crimson;
  border: 1px solid #283747;
}
</style>
