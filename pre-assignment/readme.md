## How To
- To run the server, use this command in your terminal
    -   ```
        deno run --allow-net server.ts
        ```
- This will start the server on port 8000.
- To send commands, you can use curl or tools like Postman.
    - For /rem: 
        - To save a value:
            -   ```
                curl -X POST -H "Content-Type: application/json" -d '{"name":"city", "value":"Atlantis"}' http://localhost:8000/rem
                ```
        - To retrieve a value:
            -   ```
                curl -X POST -H "Content-Type: application/json" -d '{"name":"city"}' http://localhost:8000/rem
                ```
    - For /calc:
        -   ```
            curl -X POST -H "Content-Type: application/json" -d '{"expression":"3+5"}' http://localhost:8000/calc
            ```