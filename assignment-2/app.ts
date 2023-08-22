import { serve } from "https://deno.land/std@0.150.0/http/server.ts";
import { Server } from "https://deno.land/x/socket_io@0.2.0/mod.ts";

const decoder = new TextDecoder("utf-8");
const commandsData = await Deno.readFile("commands.json");
const commands = JSON.parse(decoder.decode(commandsData));
const users = new Map();

const io = new Server({
	cors:{
		origin:true,
		credentials:true
	}
})

io.on("connection",(socket)=>{
	// IF USER CONNECTTED
	console.log(`socket user ${socket.id} connected`)
	socket.on("disconnect",(r)=>{
        const username = users.get(socket.id);
		console.log("user " + socket.id + " disconnect !!")
        io.emit("NewUserLeft",{data:`${username} left the chat`})

	})
    socket.on("UserJoin",(p)=>{
        users.set(socket.id, p.name);
        io.emit("NewUserJoined",{data:`${p.name} joined the chat`})
    })
	// LISTEN DATA FROM CLIENT 
	socket.on("newMSG",(p)=>{
        let response = p.message; // Start with the original message
        console.log(p);
        if (commands.hasOwnProperty(p.message)) {
            response = commands[p.message];
        }
        console.log(`new msg: ${response}`);
    
        // SEND TO ALL CLIENTS
        io.emit("sendallMSG", { data: { name: p.name, message: response } });
		// console.log(`new msg  : ${p}` )
		// // SEND TO ALL CLIENT
		// io.emit("sendallMSG",{data:p})
	})
})
await serve(io.handler(),{
	port:3000
})