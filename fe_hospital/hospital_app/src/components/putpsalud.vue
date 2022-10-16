<template>
  <div class="putpsalud">
    <div class="contenedor_psalud">
      <h2>Modificar Personal Salud</h2>
      <form v-on:submit.prevent="processputPsalud">
        <input
          type="number"
          v-model="medico.id"
          placeholder="id personal salud"
        />
        <br />
        <input type="text" placeholder="id_Usuario" v-model="medico.usuario" />
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
        <button type="submit">Modificar</button>
      </form>
    </div>
  </div>
</template>
<script>
import axios from "axios";
export default {
  name: "putpsalud",
  data: function () {
    return {
      medico: {
        id: "",
        username: "",
        rol: "",
        especialidad: "",
        licencia: "",
      },
    };
  },
  methods: {
    processputPsalud: function () {
      axios
        .put(
          `http://127.0.0.1:8000/personalsalud/${this.medico.id}`,
          this.medico,
          { headers: {} }
        )
        .then((result) => {
          console.log(result);
          alert("Elemento modificado");
        })
        .catch((error) => {
          console.log(error);
          alert("Error");
        });
    },
  },
};
</script>
<style>
.putpsalud {
  margin: 0;
  padding: 0%;
  height: 100%;
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.contenedor_psalud {
  border: 3px solid #283747;
  border-radius: 10px;
  width: 35%;
  height: 90%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.putpsalud h2 {
  color: #283747;
}

.putpsalud form {
  width: 70%;
}

.putpsalud input {
  height: 40px;
  width: 100%;
  box-sizing: border-box;
  padding: 10px 20px;
  margin: 5px 0;
  border: 1px solid #283747;
}

.putpsalud button {
  width: 100%;
  height: 40px;
  color: #e5e7e9;
  background: #283747;
  border: 1px solid #e5e7e9;
  border-radius: 5px;
  padding: 10px 25px;
  margin: 5px 0 25px 0;
}

.putpsalud button:hover {
  color: #e5e7e9;
  background: crimson;
  border: 1px solid #283747;
}
</style>
