import shodan
import click

# Output file to save results
OUTPUT_FILE = 'shodan_results.txt'

# Define a command-line interface using Click
@click.command()
@click.option('--api-key', prompt='Enter your Shodan API key', help='Your Shodan API key')
@click.option('--query', prompt='Enter your Shodan search query', help='The Shodan search query')
def main(api_key, query):
    try:
        # Initialize the Shodan API client with the provided API key
        api = shodan.Shodan(api_key)

        # Perform the Shodan search
        results = api.search(query)

        # Print the total number of results found
        click.echo(f"Total results found: {results['total']}")

        # Save the results to a text file
        with open(OUTPUT_FILE, 'w') as file:
            for match in results['matches']:
                file.write(f"IP: {match['ip_str']}\n")
                file.write(f"Port: {match['port']}\n")
                organization = match.get('org', 'N/A')
                file.write(f"Organization: {organization}\n")
                hostnames = ', '.join(match.get('hostnames', []))
                file.write(f"Hostnames: {hostnames}\n\n")

        click.echo(f"Results saved to {OUTPUT_FILE}")

    except shodan.APIError as e:
        click.echo(f"Shodan Error: {e}")

if __name__ == "__main__":
    # Run the main function when the script is executed
    main()
