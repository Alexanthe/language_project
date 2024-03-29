const wait = (t) => new Promise((r) => setTimeout(r, t));

const firstFunc = async () => {
    var typed = new Typed('#word', {
        stringsElement: '#typed-word',
        typeSpeed: 100,
        showCursor: false
    });
    await wait(5000); // Just to fake some wait time
}

const secondFunc = () => { // This does not need to be async
    var typed = new Typed('#promptoptions', {
        strings: ["descriptive", "narrative"],
        typeSpeed: 100,
        backSpeed: 100,
        backDelay: 1500,
        startDelay: 500,
        showCursor: true,
        loop: true
    });
}

const run2functions = async () => {
    await firstFunc();  // Await for this one
    secondFunc();       // You don't need to await for this one
};

run2functions();