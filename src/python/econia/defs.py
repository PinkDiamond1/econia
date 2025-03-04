"""Value definitions

Define all numbers/strings, etc. here so code has no unnamed values
"""

from atexit import register
from types import SimpleNamespace

account_fields = SimpleNamespace(
    authentication_key = 'authentication_key',
    sequence_number = 'sequence_number'
)
"""Account fields"""

api_url_types = SimpleNamespace(
    explorer = 'explorer',
    fullnode = 'fullnode',
    faucet = 'faucet'
)
"""Types of REST API base urls"""

build_command_fields = SimpleNamespace(
    docgen = 'docgen',
    generate = 'generate',
    print_keyfile_address = 'print-keyfile-address',
    publish = 'publish',
    rev = 'rev',
    serial = 'serial',
    substitute = 'substitute'
)
"""Command line fields for automated building process"""

Econia = 'Econia'
"""Project name"""

econia_modules = SimpleNamespace(
    capability = SimpleNamespace(
        name = 'capability',
    ),
    coins = SimpleNamespace(
        name = 'coins',
    ),
    critbit = SimpleNamespace(
        name = 'critbit'
    ),
    init = SimpleNamespace(
        name = 'init',
        entry_functions = SimpleNamespace(
            init_econia = 'init_econia'
        ),
    ),
    market = SimpleNamespace(
        name = 'market',
    ),
    open_table = SimpleNamespace(
        name = 'open_table'
    ),
    order_id = SimpleNamespace(
        name = 'order_id'
    ),
    registry = SimpleNamespace(
        name = 'registry'
    ),
    user = SimpleNamespace(
        name = 'user'
    ),
)
"""Econia Move modules with nested member specifiers"""

econia_module_publish_order = [
    [
        econia_modules.capability.name,
        econia_modules.critbit.name,
        econia_modules.order_id.name,
        econia_modules.coins.name,
        econia_modules.open_table.name,
        econia_modules.registry.name,
        econia_modules.user.name,
        econia_modules.market.name,
        econia_modules.init.name,
    ],
]
"""
Order to publish Move modules bytecode in, with sublists indicating
batched modules to load together. Individual modules should be defined
as the sole element in a list if they are to be loaded alone. If order
within sub-batches is changed loading may break, for instance among
friends, where the module declaring a friend should be listed before the
declared friend. Additionally, modules that are "used" by other modules
should be loaded before the modules that use them, and may be loaded in
a single batch, but can also be split up into separate batches.
"""

econia_paths = SimpleNamespace(
    # Relative to Move package root directory
    bytecode_dir = 'build/econia/bytecode_modules',
    # Relative to Econia repository root directory
    move_package_root = 'src/move/econia',
    # Relative to Move package root
    ss_path = 'ss',
    # Relative to Move package root
    toml_path = 'Move',
)
"""Econia Move code paths"""

e_msgs = SimpleNamespace(
    failed = 'failed',
    faucet = 'Faucet funding failed',
    path_val_collision = 'Different value already exists at provided path',
    tx_timeout = 'Transaction timeout',
    tx_submission = 'Transaction submission failed'
)
"""Error messages"""

file_extensions = SimpleNamespace(
    key = 'key',
    mv = 'mv',
    sh = 'sh',
    toml = 'toml'
)
"""Extensions for common filetypes"""

msg_sig_start_byte = 2
"""
Byte within message from transaction request post response, after which
data should be signed. Per official Aptos transaction tutorial
"""

named_addrs = SimpleNamespace(
    econia = SimpleNamespace(
        docgen = 'c0deb00c',
        address_name = 'econia',
    )
)
"""
Named addresses (without leading hex specifier). Docgen address used as
substitute in auto-generated documentation files to prevent excessively
long address names in markdown file headers."""

networks = SimpleNamespace(
    devnet = 'devnet'
)
"""Aptos cluster networks"""

payload_fields = SimpleNamespace(
    arguments = 'arguments',
    bytecode = 'bytecode',
    function = 'function',
    module_bundle_payload = 'module_bundle_payload',
    modules = 'modules',
    script_function_payload = 'script_function_payload',
    type = 'type',
    type_arguments = 'type_arguments'
)
"""Transaction payload fields"""

regex_trio_group_ids = SimpleNamespace(
    start = 1,
    middle = 2,
    end = 3
)
"""For RegEx search yielding 3 group matches"""

resource_fields = SimpleNamespace(
    coin = 'coin',
    data = 'data',
    type = 'type',
    value = 'value'
)
"""Move resource fields"""

rest_codes = SimpleNamespace(
    not_found = 404,
    processing = 202,
    success = 200
)
"""REST response codes"""

rest_path_elems = SimpleNamespace(
    accounts = 'accounts',
    mint = 'mint',
    resource = 'resource',
    resources = 'resources',
    signing_message = 'signing_message',
    transactions = 'transactions',
    txn = 'txn'
)
"""Rest API path elements"""

rest_post_headers = SimpleNamespace(
    content_type = 'Content-Type',
    application_json = 'application/json'
)
"""Rest post headers"""

rest_query_fields = SimpleNamespace(
    amount = 'amount',
    auth_key = 'auth_key',
)
"""Rest API URL query string fields"""

rest_response_fields = SimpleNamespace(
    hash = 'hash',
    message = 'message',
    pending_transaction = 'pending_transaction',
    type = 'type'
)
"""Rest response fields"""

rest_urls = {
    networks.devnet: {
        api_url_types.fullnode: 'https://fullnode.devnet.aptoslabs.com',
        api_url_types.faucet: 'https://faucet.devnet.aptoslabs.com',
        api_url_types.explorer: 'https://aptos-explorer.netlify.app'
    }
}
"""REST API urls"""

seps = SimpleNamespace(
    amp = '&',
    cln = ':',
    cma = ',',
    dot = '.',
    eq = '=',
    gt = '>',
    hex = '0x',
    lsb = '[',
    lt = '<',
    lp = '(',
    nl = '\n',
    pnd = '#',
    qm = '?',
    rp = ')',
    rsb = ']',
    sq = "'",
    sls = '/',
    sp = ' ',
    us = '_'
)
"""Separators"""

single_sig_id = b'\x00'
"""1-byte signature scheme identifier, indicating single signature"""

toml_section_names = SimpleNamespace(
    addresses = 'addresses'
)
"""Section names in Move.toml file"""

tx_defaults = SimpleNamespace(
    faucet_mint_val = 1_000_000,
    gas_currency_code = 'XUS',
    gas_unit_price = 1,
    max_gas_amount = 2000,
    timeout_in_s = 600
)
"""Default transaction metadata values per Aptos tutorial"""

tx_fields = SimpleNamespace(
    expiration_timestamp_secs = 'expiration_timestamp_secs',
    gas_currency_code = 'gas_currency_code',
    gas_unit_price = 'gas_unit_price',
    max_gas_amount = 'max_gas_amount',
    payload = 'payload',
    sender = 'sender',
    sequence_number = 'sequence_number',
    signature = 'signature',
    success = 'success',
    version = 'version'
)
"""Transaction fields"""

tx_sig_fields = SimpleNamespace(
    type = 'type',
    public_key = 'public_key',
    signature = 'signature',
    ed25519_signature = 'ed25519_signature',
)
"""Transaction signature fields"""

tx_timeout_granularity = 0.1
"""How long to wait between querying REST API for transaction status"""

util_paths = SimpleNamespace(
    # Relative to Econia repository root
    secrets_dir = '.secrets',
    # Relative to secrets directory
    old_keys = 'old',
    # Econia repository root relative to `src/jupyter`
    econia_root_rel_jupyter = '../..'
)
"""Paths to developer utility resources"""