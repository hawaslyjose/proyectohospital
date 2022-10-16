<template>
    <div class="requestuser">
        <div class="requestuserid">
            <h2>Consultar usuario</h2>
            <form v-on:submit.prevent="processRequestUser">
                <input type="number" v-model="user.id" placeholder="id usuario" >
                <br>
                <button type="submit">consultar</button>
            </form>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
export default {
    name: "RequestUser",
    data: function(){
    return {
            user:{
                id:""
            }
            
            }
        },
        methods: {
            processRequestUser: function(){
                axios.get(`http://127.0.0.1:8000/user/${this.user.id}`, {headers:{}}
                ) .then((result) => {
                   alert(JSON.stringify(result.data,null, ' '));

                }) 
                .catch((error) => {
                console.log(error)
                alert("Error");
            });
            }
        }    
    }
</script>
<style>
.requestuser{
    margin: 0;
    padding: 0%;
    height: 100%;
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    }

.requestuserid {
    border: 3px solid #283747;
    border-radius: 10px;
    width: 35%;
    height: 90%;
    background: #E5E7E9;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

.requestuser h2{
    color: #283747;
}

.requestuser form{
    width: 70%;
}

.requestuser input{
    height: 40px;
    width: 100%;
    box-sizing: border-box;
    padding: 10px 20px;
    margin: 5px 0;
    border: 1px solid #283747;
}

.requestuser button
{
    width: 100%;
    height: 40px;
    color: #E5E7E9;
    background: #283747;
    border: 1px solid #E5E7E9;
    border-radius: 5px;
    padding: 10px 25px;
    margin: 5px 0 25px 0;
}

.requestuser button:hover
{
    color: #E5E7E9;
    background: crimson;
    border: 1px solid #283747;
}
</style>