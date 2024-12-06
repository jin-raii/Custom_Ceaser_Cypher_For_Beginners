from ceaser_algo.main import encrypt, decrypt
from rich import print


def main():
    # encrypt the plaintext
    user_input = input('enter str: ')
    input_shift = int(input('enter shift: '))
    e = encrypt(user_input, input_shift)
    print(f'[bold green]Your encrypted hash:[/bold green] [bold blue]{e}[/bold blue]')

    print('[bold magenta]Decrypt[/bold magenta]')

    # decrypt the encrypted text
    user_input = input('enter decrypted hash value: ')
    d = decrypt(user_input, input_shift)
    print(f'[bold green]Your decrypted hash:[/bold green] [bold blue]{d}[/bold blue]')


if __name__ == "__main__":
    main()
