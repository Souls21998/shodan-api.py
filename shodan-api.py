import shodan

SHODAN_API_KEY = "IeUJbMfGWj0uizLQ2w5D0owu29vRw64l"

api = shodan.Shodan(SHODAN_API_KEY)

try:
    # Search Shodan
    results = api.search('apache')
    # Show the results

    print('Results found: {}'.format(results['total']))
    for result in results['matches']:
        print('IP: {}'.format(result['ip_str']))
        print(result['data'])
        print('')

except:
    print('error')
