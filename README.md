# ASCII Name Art Generator

A Python-based tool that generates random ASCII art of your name using various fonts. It uses the `pyfiglet` library to create unique, ASCII art representations of names, each time using a different font.

## Features

- **Random Fonts**: Every time you input a name, the program randomly selects a font from a collection of available fonts.
- **Interactive**: The user is prompted to input their name and can choose whether to continue generating new name art or exit the program.
- **Customizable**: Easily add or modify fonts to suit your preferences.

## Requirements

- Python 3.x
- `pyfiglet` library

You can install `pyfiglet` using pip:

```bash
pip3 install pyfiglet
```

## How to Use

1. **Clone the repository** or download the script `name_gen.py`.
   
2. **Run the script** in your terminal:

   ```bash
   python name_gen.py
   ```

3. The program will:
   - Display a "Name Generator" prompt.
   - Ask you for your name.
   - Generate ASCII art of your name using a randomly selected font.

4. After generating your name art, the program will ask if you want to generate another name art. If you type `yes`, it will continue with a new font. If you type `no` or any other input, the program will end with a "GAME OVER !!" message.

## Example Output

When you run the program and input a name like "Alice", it might look something like this:

```
 __ _   __   _  _  ____     ___  ____  __ _  ____  ____   __  ____  __  ____ 
(  ( \ / _\ ( \/ )(  __)   / __)(  __)(  ( \(  __)(  _ \ / _\(_  _)/  \(  _ \
/    //    \/ \/ \ ) _)   ( (_ \ ) _) /    / ) _)  )   //    \ )( (  O ))   /
\_)__)\_/\_/\_)(_/(____)   \___/(____)\_)__)(____)(__\_)\_/\_/(__) \__/(__\_)

What name would you like?: Alice
Welcome to the Name Generator!
This program will generate a random ascii art with your name for you.
  __   __    __  ___  ____ 
 / _\ (  )  (  )/ __)(  __)
/    \/ (_/\ )(( (__  ) _) 
\_/\_/\____/(__)\___)(____)

Exit: yes
  ___   __   _  _  ____     __   _  _  ____  ____    _  _   
 / __) / _\ ( \/ )(  __)   /  \ / )( \(  __)(  _ \  / \/ \  
( (_ \/    \/ \/ \ ) _)   (  O )\ \/ / ) _)  )   /  \_/\_/  
 \___/\_/\_/\_)(_/(____)   \__/  \__/ (____)(__\_)  (_)(_)  

```

## Code Explanation

- **`random.seed()`**: Initializes the random number generator.
- **`figlet.getFonts()`**: Retrieves all available fonts.
- **`figlet.setFont()`**: Sets the current font to a randomly selected one.
- **`figlet.renderText()`**: Renders the input text (name) in ASCII art using the selected font.
- **`input('Exit: ')`**: Prompts the user to decide whether they want to exit or generate another name art.

## License

This project is licensed under the MIT License.
