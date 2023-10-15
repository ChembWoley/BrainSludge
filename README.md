
![image](https://github.com/ChembWoley/BrainSludge/assets/121530631/5e0e3b42-537c-4cd9-8456-92f995e08bee)

BrainSludge is a Brainfuck superset that adds several new features and commands to the traditional Brainfuck language, making it more versatile and powerful. This README.md file will provide you with an overview of BrainSludge, how to use it, and the various features it offers. btw its 500000x slower than brainfuck so thats something lol

## Features

BrainSludge introduces the following features to the traditional Brainfuck language:

1. **Comments:** You can add comments to your code by using the `#` symbol. Any text after `#` on a line is treated as a comment and will be ignored by the interpreter.

2. **Debug Mode:** You can enable or disable the debug mode by using the `~` symbol. When debug mode is enabled, the interpreter will print additional debugging information, including the current byte value and the executed character at each step.

3. **Output Formatting:** BrainSludge provides additional output formatting options:
   - `.`: Print the character associated with the current byte (like in Brainfuck).
   - `^`: Print the numeric value of the current byte.
   - `_`: Print a newline character.

4. **Loops:** BrainSludge allows you to define loops using the `[` and `]` symbols, similar to Brainfuck. Loops are executed as long as the current byte is not equal to 0.

5. **Conditional Execution:** You can use the `{` and `}` symbols to conditionally execute code based on the current byte's value. The code inside the braces will be executed if the current byte is not equal to 0.

6. **Input:** Use the `,` symbol to read a character from the user and store its ASCII value in the current byte.

7. **Imports:** You can import and run code from external files using the `|` symbol. Specify the filename as the content of the line immediately following the `|` symbol.

8. **Jumps and Labels:** You can create jumps and labels using the `:` symbol. Jump to a label by specifying its byte position as the current byte value using the `@` symbol. This can be used for control flow and subroutines.

## How to Use BrainSludge

To run a BrainSludge program, you need to have BrainSludge installed. Here are the steps to execute a BrainSludge program:

1. Save your BrainSludge code in a file with a `.bsl` extension (or any other preferred extension).

2. Open your terminal or command prompt.

3. Run the BrainSludge interpreter with your BrainSludge code as a command-line argument:

   ```sh
   therealbrainsludgerealtimeinterpreter your_code.bsl
   ```

   Replace `your_code.bsl` with the path to your BrainSludge code file.

4. Your BrainSludge program will be executed, and the output will be displayed in the terminal.

## Example

Here's a simple BrainSludge program that prints "Hello, World!" three times and exits:

```BrainSludge
# "Hello, World!" to the power of three program in BrainSludge
++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++.
>:
```

To run this program, save it to a file with a `.bsl` extension and follow the execution steps mentioned above.

## Contributing

If you're interested in contributing to BrainSludge or have any suggestions, please feel free to open issues or pull requests on the [GitHub repository](https://github.com/ChembWoley/BrainSludge).

## License

This BrainSludge interpreter is provided under the [MIT License](LICENSE).

Happy coding with BrainSludge!
