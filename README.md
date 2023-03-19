Cloudflare DNS Updater
======================

This Python library provides a simple way to update DNS records using the Cloudflare API. It includes a main function called `update_dns` that updates a specific DNS record by its name.

Installation
------------

To use this library, add it as a submodule:

    git submodule add src/cloudflare-api https://github.com/elfefe/cloudflare-api

Usage
-----

The following example demonstrates how to use the library:

```
import update_dns  

# Authentication
auth = {     
    "email": "your_email@example.com",     
    "api_key": "your_api_key", 
}  

# DNS configuration
dns = "example.com" 
dns_fullname = "subdomain.example.com"  

# Modifications 
modifs = {     
    "content": "192.168.1.1", 
}  

# Update the DNS record 
response = update_dns(auth, dns, dns_fullname, **modifs) 

print(response)`
```
Replace `"your_email@example.com"` and `"your_api_key"` with your Cloudflare account email and API key, respectively. Set `dns` to your domain name and `dns_fullname` to the full name of the DNS record you want to update. Use the `modifs` dictionary to specify the modifications you want to make to the DNS record.

Functions
---------

### update\_dns(auth, dns, dns\_fullname, \*\*modifs)

Updates a DNS record with the specified modifications.

**Arguments:**

*   `auth`: A dictionary with the following keys:
    *   `email`: Your Cloudflare account email.
    *   `api_key`: Your Cloudflare API key.
*   `dns`: The domain name for which the DNS record should be updated.
*   `dns_fullname`: The full name of the DNS record to be updated.
*   `**modifs`: A dictionary containing the key-value pairs for the modifications you want to make to the DNS record.

**Returns:**

*   A dictionary containing the response from the Cloudflare API.

**Raises:**

*   `Exception`: If the specified DNS zone is not found or the specified DNS record is not found.

License
-------

This project is released under the [MIT License](https://opensource.org/licenses/MIT).