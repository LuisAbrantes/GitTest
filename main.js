class Person {
    constructor() { }
    initialize(name, age) {
        this.name = name;
        this.age = age;
    }
}

class Teacher {
    constructor() {};
    teach(subject) {
        console.log(this.name + ' is now teaching ' + subject);
    }
}
Teacher.prototype = new Person();

var him = new Teacher();

him.initialize("Adam", 45);
him.teach("Inheritance");