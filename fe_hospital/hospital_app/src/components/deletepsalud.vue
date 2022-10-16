<template>
  <div class="deletepsalud">
    <div class="contenedor_psalud">
      <h2>Eliminar Personal Salud</h2>
      <form v-on:submit.prevent="processDeletePsalud">
        <input
          type="number"
          v-model="medico.id"
          placeholder="id personal salud"
        />
        <br />
        <button type="submit">Eliminar</button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "deletepsalud",
  data: function () {
    return {
      medico: {
        id: "",
      },
    };
  },
  methods: {
    processDeletePsalud: function () {
      axios
        .delete(`http://127.0.0.1:8000/personalsalud/${this.medico.id}`, {
          headers: {},
        })
        .then((result) => {
          alert("Elemento eliminado");
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
.deletepsalud {
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
  height: 110%;
  background: #e5e7e9;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.deletepsalud h2 {
  color: #283747;
}

.deletepsalud form {
  width: 70%;
}

.deletepsalud input {
  height: 40px;
  width: 100%;
  box-sizing: border-box;
  padding: 10px 20px;
  margin: 5px 0;
  border: 1px solid #283747;
}

.deletepsalud button {
  width: 100%;
  height: 40px;
  color: #e5e7e9;
  background: #283747;
  border: 1px solid #e5e7e9;
  border-radius: 5px;
  padding: 10px 25px;
  margin: 5px 0 25px 0;
}

.deletepsalud button:hover {
  color: #e5e7e9;
  background: crimson;
  border: 1px solid #283747;
}
</style>
