var messages = require('./service_pb');
var services = require('./service_grpc_pb');
var grpc = require('@grpc/grpc-js');
var { stdin, stdout } = process;

function prompt(question) {
  return new Promise((resolve, reject) => {
    stdin.resume();
    stdout.write(question);

    stdin.on('data', data => resolve(data.toString().trim()));
    stdin.on('error', err => reject(err));
  });
}

async function main() {
    host = process.env.host;
    port = process.env.port;
    if (host === undefined) {
        host = '127.0.0.1';
    }
    if (port === undefined) {
        port = 8008;
    }

    var target = host + ':' + port;
    var client = new services.CalculatorClient(target, grpc.credentials.createInsecure());
    var request = new messages.EquationMessage();
    var choice = undefined;

    while (true) {

        try {
            choice = await prompt("Choose action\n1. Solve equation.\n2. Exit.\n");
            choice = parseInt(choice);
        }
        catch(error) {
            console.log('Some error occurred');
            console.log(error);
        }
        if (choice === 2) {
            console.log('Exiting');
            process.exit();
        }
        try {
            var a = await prompt("Enter A coefficient: ");
            var b = await prompt("Enter B coefficient: ");
            var c = await prompt("Enter C coefficient: ");
        }
        catch(error) {
            console.log('Some error occurred');
            console.log(error);
        }

        request.setA(a);
        request.setB(b);
        request.setC(c);

        client.solve(request, (err, response) => {
            if (!err) {
                console.log('Got response!');
                var x1 = response.getX1();
                var x2 = response.getX2();
                var hasSolution = response.getRealsolutionexists();
                console.log(hasSolution);
                console.log(x1);
                console.log(x2);
            }
            else {
                console.log('The following error occurred');
                console.log(err);
            }
        });
    }
}

main();
