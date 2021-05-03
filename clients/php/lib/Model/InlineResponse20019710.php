<?php
/**
 * InlineResponse20019710
 *
 * PHP version 5
 *
 * @category Class
 * @package  OpenAPI\Client
 * @author   OpenAPI Generator team
 * @link     https://openapi-generator.tech
 */

/**
 * untitled API
 *
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 5229
 * 
 * Generated by: https://openapi-generator.tech
 * OpenAPI Generator version: 4.3.1
 */

/**
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

namespace OpenAPI\Client\Model;

use \ArrayAccess;
use \OpenAPI\Client\ObjectSerializer;

/**
 * InlineResponse20019710 Class Doc Comment
 *
 * @category Class
 * @package  OpenAPI\Client
 * @author   OpenAPI Generator team
 * @link     https://openapi-generator.tech
 */
class InlineResponse20019710 implements ModelInterface, ArrayAccess
{
    const DISCRIMINATOR = null;

    /**
      * The original name of the model.
      *
      * @var string
      */
    protected static $openAPIModelName = 'inline_response_200_19_7_1_0';

    /**
      * Array of property to type mappings. Used for (de)serialization
      *
      * @var string[]
      */
    protected static $openAPITypes = [
        'ziti_cli_linux_binary_sha_1' => 'string',
        'ziti_tunnel_linux_binary' => 'string',
        'ziti_tunnel_linux_binary_sha_1' => 'string',
        'ziti_controller_binary' => 'string',
        'ziti_cli_linux_binary_md5' => 'string',
        'ziti_router_linux_binary_sha_1' => 'string',
        'ziti_router_linux_binary_sha_256' => 'string',
        'ziti_router_linux_binary_md5' => 'string',
        'ziti_windows_desktop_edge' => 'string',
        'ziti_mac_desktop_edge' => 'string',
        'ziti_controller_binary_sha_1' => 'string',
        'ziti_controller_binary_md5' => 'string',
        'ziti_controller_binary_sha_256' => 'string',
        'ziti_ios_edge' => 'string',
        'ziti_cli_linux_binary' => 'string',
        'ziti_version' => 'string',
        'ziti_router_linux_binary' => 'string',
        'ziti_tunnel_linux_binary_sha_256' => 'string',
        'ziti_android_edge' => 'string',
        'ziti_tunnel_linux_binary_md5' => 'string',
        'ziti_cli_linux_binary_sha_256' => 'string',
        'active' => 'bool'
    ];

    /**
      * Array of property to format mappings. Used for (de)serialization
      *
      * @var string[]
      */
    protected static $openAPIFormats = [
        'ziti_cli_linux_binary_sha_1' => null,
        'ziti_tunnel_linux_binary' => null,
        'ziti_tunnel_linux_binary_sha_1' => null,
        'ziti_controller_binary' => null,
        'ziti_cli_linux_binary_md5' => null,
        'ziti_router_linux_binary_sha_1' => null,
        'ziti_router_linux_binary_sha_256' => null,
        'ziti_router_linux_binary_md5' => null,
        'ziti_windows_desktop_edge' => null,
        'ziti_mac_desktop_edge' => null,
        'ziti_controller_binary_sha_1' => null,
        'ziti_controller_binary_md5' => null,
        'ziti_controller_binary_sha_256' => null,
        'ziti_ios_edge' => null,
        'ziti_cli_linux_binary' => null,
        'ziti_version' => null,
        'ziti_router_linux_binary' => null,
        'ziti_tunnel_linux_binary_sha_256' => null,
        'ziti_android_edge' => null,
        'ziti_tunnel_linux_binary_md5' => null,
        'ziti_cli_linux_binary_sha_256' => null,
        'active' => null
    ];

    /**
     * Array of property to type mappings. Used for (de)serialization
     *
     * @return array
     */
    public static function openAPITypes()
    {
        return self::$openAPITypes;
    }

    /**
     * Array of property to format mappings. Used for (de)serialization
     *
     * @return array
     */
    public static function openAPIFormats()
    {
        return self::$openAPIFormats;
    }

    /**
     * Array of attributes where the key is the local name,
     * and the value is the original name
     *
     * @var string[]
     */
    protected static $attributeMap = [
        'ziti_cli_linux_binary_sha_1' => 'zitiCliLinuxBinary.sha-1',
        'ziti_tunnel_linux_binary' => 'zitiTunnelLinuxBinary',
        'ziti_tunnel_linux_binary_sha_1' => 'zitiTunnelLinuxBinary.sha-1',
        'ziti_controller_binary' => 'zitiControllerBinary',
        'ziti_cli_linux_binary_md5' => 'zitiCliLinuxBinary.md5',
        'ziti_router_linux_binary_sha_1' => 'zitiRouterLinuxBinary.sha-1',
        'ziti_router_linux_binary_sha_256' => 'zitiRouterLinuxBinary.sha-256',
        'ziti_router_linux_binary_md5' => 'zitiRouterLinuxBinary.md5',
        'ziti_windows_desktop_edge' => 'zitiWindowsDesktopEdge',
        'ziti_mac_desktop_edge' => 'zitiMacDesktopEdge',
        'ziti_controller_binary_sha_1' => 'zitiControllerBinary.sha-1',
        'ziti_controller_binary_md5' => 'zitiControllerBinary.md5',
        'ziti_controller_binary_sha_256' => 'zitiControllerBinary.sha-256',
        'ziti_ios_edge' => 'zitiIosEdge',
        'ziti_cli_linux_binary' => 'zitiCliLinuxBinary',
        'ziti_version' => 'zitiVersion',
        'ziti_router_linux_binary' => 'zitiRouterLinuxBinary',
        'ziti_tunnel_linux_binary_sha_256' => 'zitiTunnelLinuxBinary.sha-256',
        'ziti_android_edge' => 'zitiAndroidEdge',
        'ziti_tunnel_linux_binary_md5' => 'zitiTunnelLinuxBinary.md5',
        'ziti_cli_linux_binary_sha_256' => 'zitiCliLinuxBinary.sha-256',
        'active' => 'active'
    ];

    /**
     * Array of attributes to setter functions (for deserialization of responses)
     *
     * @var string[]
     */
    protected static $setters = [
        'ziti_cli_linux_binary_sha_1' => 'setZitiCliLinuxBinarySha1',
        'ziti_tunnel_linux_binary' => 'setZitiTunnelLinuxBinary',
        'ziti_tunnel_linux_binary_sha_1' => 'setZitiTunnelLinuxBinarySha1',
        'ziti_controller_binary' => 'setZitiControllerBinary',
        'ziti_cli_linux_binary_md5' => 'setZitiCliLinuxBinaryMd5',
        'ziti_router_linux_binary_sha_1' => 'setZitiRouterLinuxBinarySha1',
        'ziti_router_linux_binary_sha_256' => 'setZitiRouterLinuxBinarySha256',
        'ziti_router_linux_binary_md5' => 'setZitiRouterLinuxBinaryMd5',
        'ziti_windows_desktop_edge' => 'setZitiWindowsDesktopEdge',
        'ziti_mac_desktop_edge' => 'setZitiMacDesktopEdge',
        'ziti_controller_binary_sha_1' => 'setZitiControllerBinarySha1',
        'ziti_controller_binary_md5' => 'setZitiControllerBinaryMd5',
        'ziti_controller_binary_sha_256' => 'setZitiControllerBinarySha256',
        'ziti_ios_edge' => 'setZitiIosEdge',
        'ziti_cli_linux_binary' => 'setZitiCliLinuxBinary',
        'ziti_version' => 'setZitiVersion',
        'ziti_router_linux_binary' => 'setZitiRouterLinuxBinary',
        'ziti_tunnel_linux_binary_sha_256' => 'setZitiTunnelLinuxBinarySha256',
        'ziti_android_edge' => 'setZitiAndroidEdge',
        'ziti_tunnel_linux_binary_md5' => 'setZitiTunnelLinuxBinaryMd5',
        'ziti_cli_linux_binary_sha_256' => 'setZitiCliLinuxBinarySha256',
        'active' => 'setActive'
    ];

    /**
     * Array of attributes to getter functions (for serialization of requests)
     *
     * @var string[]
     */
    protected static $getters = [
        'ziti_cli_linux_binary_sha_1' => 'getZitiCliLinuxBinarySha1',
        'ziti_tunnel_linux_binary' => 'getZitiTunnelLinuxBinary',
        'ziti_tunnel_linux_binary_sha_1' => 'getZitiTunnelLinuxBinarySha1',
        'ziti_controller_binary' => 'getZitiControllerBinary',
        'ziti_cli_linux_binary_md5' => 'getZitiCliLinuxBinaryMd5',
        'ziti_router_linux_binary_sha_1' => 'getZitiRouterLinuxBinarySha1',
        'ziti_router_linux_binary_sha_256' => 'getZitiRouterLinuxBinarySha256',
        'ziti_router_linux_binary_md5' => 'getZitiRouterLinuxBinaryMd5',
        'ziti_windows_desktop_edge' => 'getZitiWindowsDesktopEdge',
        'ziti_mac_desktop_edge' => 'getZitiMacDesktopEdge',
        'ziti_controller_binary_sha_1' => 'getZitiControllerBinarySha1',
        'ziti_controller_binary_md5' => 'getZitiControllerBinaryMd5',
        'ziti_controller_binary_sha_256' => 'getZitiControllerBinarySha256',
        'ziti_ios_edge' => 'getZitiIosEdge',
        'ziti_cli_linux_binary' => 'getZitiCliLinuxBinary',
        'ziti_version' => 'getZitiVersion',
        'ziti_router_linux_binary' => 'getZitiRouterLinuxBinary',
        'ziti_tunnel_linux_binary_sha_256' => 'getZitiTunnelLinuxBinarySha256',
        'ziti_android_edge' => 'getZitiAndroidEdge',
        'ziti_tunnel_linux_binary_md5' => 'getZitiTunnelLinuxBinaryMd5',
        'ziti_cli_linux_binary_sha_256' => 'getZitiCliLinuxBinarySha256',
        'active' => 'getActive'
    ];

    /**
     * Array of attributes where the key is the local name,
     * and the value is the original name
     *
     * @return array
     */
    public static function attributeMap()
    {
        return self::$attributeMap;
    }

    /**
     * Array of attributes to setter functions (for deserialization of responses)
     *
     * @return array
     */
    public static function setters()
    {
        return self::$setters;
    }

    /**
     * Array of attributes to getter functions (for serialization of requests)
     *
     * @return array
     */
    public static function getters()
    {
        return self::$getters;
    }

    /**
     * The original name of the model.
     *
     * @return string
     */
    public function getModelName()
    {
        return self::$openAPIModelName;
    }

    

    

    /**
     * Associative array for storing property values
     *
     * @var mixed[]
     */
    protected $container = [];

    /**
     * Constructor
     *
     * @param mixed[] $data Associated array of property values
     *                      initializing the model
     */
    public function __construct(array $data = null)
    {
        $this->container['ziti_cli_linux_binary_sha_1'] = isset($data['ziti_cli_linux_binary_sha_1']) ? $data['ziti_cli_linux_binary_sha_1'] : null;
        $this->container['ziti_tunnel_linux_binary'] = isset($data['ziti_tunnel_linux_binary']) ? $data['ziti_tunnel_linux_binary'] : null;
        $this->container['ziti_tunnel_linux_binary_sha_1'] = isset($data['ziti_tunnel_linux_binary_sha_1']) ? $data['ziti_tunnel_linux_binary_sha_1'] : null;
        $this->container['ziti_controller_binary'] = isset($data['ziti_controller_binary']) ? $data['ziti_controller_binary'] : null;
        $this->container['ziti_cli_linux_binary_md5'] = isset($data['ziti_cli_linux_binary_md5']) ? $data['ziti_cli_linux_binary_md5'] : null;
        $this->container['ziti_router_linux_binary_sha_1'] = isset($data['ziti_router_linux_binary_sha_1']) ? $data['ziti_router_linux_binary_sha_1'] : null;
        $this->container['ziti_router_linux_binary_sha_256'] = isset($data['ziti_router_linux_binary_sha_256']) ? $data['ziti_router_linux_binary_sha_256'] : null;
        $this->container['ziti_router_linux_binary_md5'] = isset($data['ziti_router_linux_binary_md5']) ? $data['ziti_router_linux_binary_md5'] : null;
        $this->container['ziti_windows_desktop_edge'] = isset($data['ziti_windows_desktop_edge']) ? $data['ziti_windows_desktop_edge'] : null;
        $this->container['ziti_mac_desktop_edge'] = isset($data['ziti_mac_desktop_edge']) ? $data['ziti_mac_desktop_edge'] : null;
        $this->container['ziti_controller_binary_sha_1'] = isset($data['ziti_controller_binary_sha_1']) ? $data['ziti_controller_binary_sha_1'] : null;
        $this->container['ziti_controller_binary_md5'] = isset($data['ziti_controller_binary_md5']) ? $data['ziti_controller_binary_md5'] : null;
        $this->container['ziti_controller_binary_sha_256'] = isset($data['ziti_controller_binary_sha_256']) ? $data['ziti_controller_binary_sha_256'] : null;
        $this->container['ziti_ios_edge'] = isset($data['ziti_ios_edge']) ? $data['ziti_ios_edge'] : null;
        $this->container['ziti_cli_linux_binary'] = isset($data['ziti_cli_linux_binary']) ? $data['ziti_cli_linux_binary'] : null;
        $this->container['ziti_version'] = isset($data['ziti_version']) ? $data['ziti_version'] : null;
        $this->container['ziti_router_linux_binary'] = isset($data['ziti_router_linux_binary']) ? $data['ziti_router_linux_binary'] : null;
        $this->container['ziti_tunnel_linux_binary_sha_256'] = isset($data['ziti_tunnel_linux_binary_sha_256']) ? $data['ziti_tunnel_linux_binary_sha_256'] : null;
        $this->container['ziti_android_edge'] = isset($data['ziti_android_edge']) ? $data['ziti_android_edge'] : null;
        $this->container['ziti_tunnel_linux_binary_md5'] = isset($data['ziti_tunnel_linux_binary_md5']) ? $data['ziti_tunnel_linux_binary_md5'] : null;
        $this->container['ziti_cli_linux_binary_sha_256'] = isset($data['ziti_cli_linux_binary_sha_256']) ? $data['ziti_cli_linux_binary_sha_256'] : null;
        $this->container['active'] = isset($data['active']) ? $data['active'] : null;
    }

    /**
     * Show all the invalid properties with reasons.
     *
     * @return array invalid properties with reasons
     */
    public function listInvalidProperties()
    {
        $invalidProperties = [];

        if ($this->container['ziti_cli_linux_binary_sha_1'] === null) {
            $invalidProperties[] = "'ziti_cli_linux_binary_sha_1' can't be null";
        }
        if ($this->container['ziti_tunnel_linux_binary'] === null) {
            $invalidProperties[] = "'ziti_tunnel_linux_binary' can't be null";
        }
        if ($this->container['ziti_tunnel_linux_binary_sha_1'] === null) {
            $invalidProperties[] = "'ziti_tunnel_linux_binary_sha_1' can't be null";
        }
        if ($this->container['ziti_controller_binary'] === null) {
            $invalidProperties[] = "'ziti_controller_binary' can't be null";
        }
        if ($this->container['ziti_cli_linux_binary_md5'] === null) {
            $invalidProperties[] = "'ziti_cli_linux_binary_md5' can't be null";
        }
        if ($this->container['ziti_router_linux_binary_sha_1'] === null) {
            $invalidProperties[] = "'ziti_router_linux_binary_sha_1' can't be null";
        }
        if ($this->container['ziti_router_linux_binary_sha_256'] === null) {
            $invalidProperties[] = "'ziti_router_linux_binary_sha_256' can't be null";
        }
        if ($this->container['ziti_router_linux_binary_md5'] === null) {
            $invalidProperties[] = "'ziti_router_linux_binary_md5' can't be null";
        }
        if ($this->container['ziti_windows_desktop_edge'] === null) {
            $invalidProperties[] = "'ziti_windows_desktop_edge' can't be null";
        }
        if ($this->container['ziti_mac_desktop_edge'] === null) {
            $invalidProperties[] = "'ziti_mac_desktop_edge' can't be null";
        }
        if ($this->container['ziti_controller_binary_sha_1'] === null) {
            $invalidProperties[] = "'ziti_controller_binary_sha_1' can't be null";
        }
        if ($this->container['ziti_controller_binary_md5'] === null) {
            $invalidProperties[] = "'ziti_controller_binary_md5' can't be null";
        }
        if ($this->container['ziti_controller_binary_sha_256'] === null) {
            $invalidProperties[] = "'ziti_controller_binary_sha_256' can't be null";
        }
        if ($this->container['ziti_ios_edge'] === null) {
            $invalidProperties[] = "'ziti_ios_edge' can't be null";
        }
        if ($this->container['ziti_cli_linux_binary'] === null) {
            $invalidProperties[] = "'ziti_cli_linux_binary' can't be null";
        }
        if ($this->container['ziti_version'] === null) {
            $invalidProperties[] = "'ziti_version' can't be null";
        }
        if ($this->container['ziti_router_linux_binary'] === null) {
            $invalidProperties[] = "'ziti_router_linux_binary' can't be null";
        }
        if ($this->container['ziti_tunnel_linux_binary_sha_256'] === null) {
            $invalidProperties[] = "'ziti_tunnel_linux_binary_sha_256' can't be null";
        }
        if ($this->container['ziti_android_edge'] === null) {
            $invalidProperties[] = "'ziti_android_edge' can't be null";
        }
        if ($this->container['ziti_tunnel_linux_binary_md5'] === null) {
            $invalidProperties[] = "'ziti_tunnel_linux_binary_md5' can't be null";
        }
        if ($this->container['ziti_cli_linux_binary_sha_256'] === null) {
            $invalidProperties[] = "'ziti_cli_linux_binary_sha_256' can't be null";
        }
        if ($this->container['active'] === null) {
            $invalidProperties[] = "'active' can't be null";
        }
        return $invalidProperties;
    }

    /**
     * Validate all the properties in the model
     * return true if all passed
     *
     * @return bool True if all properties are valid
     */
    public function valid()
    {
        return count($this->listInvalidProperties()) === 0;
    }


    /**
     * Gets ziti_cli_linux_binary_sha_1
     *
     * @return string
     */
    public function getZitiCliLinuxBinarySha1()
    {
        return $this->container['ziti_cli_linux_binary_sha_1'];
    }

    /**
     * Sets ziti_cli_linux_binary_sha_1
     *
     * @param string $ziti_cli_linux_binary_sha_1 ziti_cli_linux_binary_sha_1
     *
     * @return $this
     */
    public function setZitiCliLinuxBinarySha1($ziti_cli_linux_binary_sha_1)
    {
        $this->container['ziti_cli_linux_binary_sha_1'] = $ziti_cli_linux_binary_sha_1;

        return $this;
    }

    /**
     * Gets ziti_tunnel_linux_binary
     *
     * @return string
     */
    public function getZitiTunnelLinuxBinary()
    {
        return $this->container['ziti_tunnel_linux_binary'];
    }

    /**
     * Sets ziti_tunnel_linux_binary
     *
     * @param string $ziti_tunnel_linux_binary ziti_tunnel_linux_binary
     *
     * @return $this
     */
    public function setZitiTunnelLinuxBinary($ziti_tunnel_linux_binary)
    {
        $this->container['ziti_tunnel_linux_binary'] = $ziti_tunnel_linux_binary;

        return $this;
    }

    /**
     * Gets ziti_tunnel_linux_binary_sha_1
     *
     * @return string
     */
    public function getZitiTunnelLinuxBinarySha1()
    {
        return $this->container['ziti_tunnel_linux_binary_sha_1'];
    }

    /**
     * Sets ziti_tunnel_linux_binary_sha_1
     *
     * @param string $ziti_tunnel_linux_binary_sha_1 ziti_tunnel_linux_binary_sha_1
     *
     * @return $this
     */
    public function setZitiTunnelLinuxBinarySha1($ziti_tunnel_linux_binary_sha_1)
    {
        $this->container['ziti_tunnel_linux_binary_sha_1'] = $ziti_tunnel_linux_binary_sha_1;

        return $this;
    }

    /**
     * Gets ziti_controller_binary
     *
     * @return string
     */
    public function getZitiControllerBinary()
    {
        return $this->container['ziti_controller_binary'];
    }

    /**
     * Sets ziti_controller_binary
     *
     * @param string $ziti_controller_binary ziti_controller_binary
     *
     * @return $this
     */
    public function setZitiControllerBinary($ziti_controller_binary)
    {
        $this->container['ziti_controller_binary'] = $ziti_controller_binary;

        return $this;
    }

    /**
     * Gets ziti_cli_linux_binary_md5
     *
     * @return string
     */
    public function getZitiCliLinuxBinaryMd5()
    {
        return $this->container['ziti_cli_linux_binary_md5'];
    }

    /**
     * Sets ziti_cli_linux_binary_md5
     *
     * @param string $ziti_cli_linux_binary_md5 ziti_cli_linux_binary_md5
     *
     * @return $this
     */
    public function setZitiCliLinuxBinaryMd5($ziti_cli_linux_binary_md5)
    {
        $this->container['ziti_cli_linux_binary_md5'] = $ziti_cli_linux_binary_md5;

        return $this;
    }

    /**
     * Gets ziti_router_linux_binary_sha_1
     *
     * @return string
     */
    public function getZitiRouterLinuxBinarySha1()
    {
        return $this->container['ziti_router_linux_binary_sha_1'];
    }

    /**
     * Sets ziti_router_linux_binary_sha_1
     *
     * @param string $ziti_router_linux_binary_sha_1 ziti_router_linux_binary_sha_1
     *
     * @return $this
     */
    public function setZitiRouterLinuxBinarySha1($ziti_router_linux_binary_sha_1)
    {
        $this->container['ziti_router_linux_binary_sha_1'] = $ziti_router_linux_binary_sha_1;

        return $this;
    }

    /**
     * Gets ziti_router_linux_binary_sha_256
     *
     * @return string
     */
    public function getZitiRouterLinuxBinarySha256()
    {
        return $this->container['ziti_router_linux_binary_sha_256'];
    }

    /**
     * Sets ziti_router_linux_binary_sha_256
     *
     * @param string $ziti_router_linux_binary_sha_256 ziti_router_linux_binary_sha_256
     *
     * @return $this
     */
    public function setZitiRouterLinuxBinarySha256($ziti_router_linux_binary_sha_256)
    {
        $this->container['ziti_router_linux_binary_sha_256'] = $ziti_router_linux_binary_sha_256;

        return $this;
    }

    /**
     * Gets ziti_router_linux_binary_md5
     *
     * @return string
     */
    public function getZitiRouterLinuxBinaryMd5()
    {
        return $this->container['ziti_router_linux_binary_md5'];
    }

    /**
     * Sets ziti_router_linux_binary_md5
     *
     * @param string $ziti_router_linux_binary_md5 ziti_router_linux_binary_md5
     *
     * @return $this
     */
    public function setZitiRouterLinuxBinaryMd5($ziti_router_linux_binary_md5)
    {
        $this->container['ziti_router_linux_binary_md5'] = $ziti_router_linux_binary_md5;

        return $this;
    }

    /**
     * Gets ziti_windows_desktop_edge
     *
     * @return string
     */
    public function getZitiWindowsDesktopEdge()
    {
        return $this->container['ziti_windows_desktop_edge'];
    }

    /**
     * Sets ziti_windows_desktop_edge
     *
     * @param string $ziti_windows_desktop_edge ziti_windows_desktop_edge
     *
     * @return $this
     */
    public function setZitiWindowsDesktopEdge($ziti_windows_desktop_edge)
    {
        $this->container['ziti_windows_desktop_edge'] = $ziti_windows_desktop_edge;

        return $this;
    }

    /**
     * Gets ziti_mac_desktop_edge
     *
     * @return string
     */
    public function getZitiMacDesktopEdge()
    {
        return $this->container['ziti_mac_desktop_edge'];
    }

    /**
     * Sets ziti_mac_desktop_edge
     *
     * @param string $ziti_mac_desktop_edge ziti_mac_desktop_edge
     *
     * @return $this
     */
    public function setZitiMacDesktopEdge($ziti_mac_desktop_edge)
    {
        $this->container['ziti_mac_desktop_edge'] = $ziti_mac_desktop_edge;

        return $this;
    }

    /**
     * Gets ziti_controller_binary_sha_1
     *
     * @return string
     */
    public function getZitiControllerBinarySha1()
    {
        return $this->container['ziti_controller_binary_sha_1'];
    }

    /**
     * Sets ziti_controller_binary_sha_1
     *
     * @param string $ziti_controller_binary_sha_1 ziti_controller_binary_sha_1
     *
     * @return $this
     */
    public function setZitiControllerBinarySha1($ziti_controller_binary_sha_1)
    {
        $this->container['ziti_controller_binary_sha_1'] = $ziti_controller_binary_sha_1;

        return $this;
    }

    /**
     * Gets ziti_controller_binary_md5
     *
     * @return string
     */
    public function getZitiControllerBinaryMd5()
    {
        return $this->container['ziti_controller_binary_md5'];
    }

    /**
     * Sets ziti_controller_binary_md5
     *
     * @param string $ziti_controller_binary_md5 ziti_controller_binary_md5
     *
     * @return $this
     */
    public function setZitiControllerBinaryMd5($ziti_controller_binary_md5)
    {
        $this->container['ziti_controller_binary_md5'] = $ziti_controller_binary_md5;

        return $this;
    }

    /**
     * Gets ziti_controller_binary_sha_256
     *
     * @return string
     */
    public function getZitiControllerBinarySha256()
    {
        return $this->container['ziti_controller_binary_sha_256'];
    }

    /**
     * Sets ziti_controller_binary_sha_256
     *
     * @param string $ziti_controller_binary_sha_256 ziti_controller_binary_sha_256
     *
     * @return $this
     */
    public function setZitiControllerBinarySha256($ziti_controller_binary_sha_256)
    {
        $this->container['ziti_controller_binary_sha_256'] = $ziti_controller_binary_sha_256;

        return $this;
    }

    /**
     * Gets ziti_ios_edge
     *
     * @return string
     */
    public function getZitiIosEdge()
    {
        return $this->container['ziti_ios_edge'];
    }

    /**
     * Sets ziti_ios_edge
     *
     * @param string $ziti_ios_edge ziti_ios_edge
     *
     * @return $this
     */
    public function setZitiIosEdge($ziti_ios_edge)
    {
        $this->container['ziti_ios_edge'] = $ziti_ios_edge;

        return $this;
    }

    /**
     * Gets ziti_cli_linux_binary
     *
     * @return string
     */
    public function getZitiCliLinuxBinary()
    {
        return $this->container['ziti_cli_linux_binary'];
    }

    /**
     * Sets ziti_cli_linux_binary
     *
     * @param string $ziti_cli_linux_binary ziti_cli_linux_binary
     *
     * @return $this
     */
    public function setZitiCliLinuxBinary($ziti_cli_linux_binary)
    {
        $this->container['ziti_cli_linux_binary'] = $ziti_cli_linux_binary;

        return $this;
    }

    /**
     * Gets ziti_version
     *
     * @return string
     */
    public function getZitiVersion()
    {
        return $this->container['ziti_version'];
    }

    /**
     * Sets ziti_version
     *
     * @param string $ziti_version ziti_version
     *
     * @return $this
     */
    public function setZitiVersion($ziti_version)
    {
        $this->container['ziti_version'] = $ziti_version;

        return $this;
    }

    /**
     * Gets ziti_router_linux_binary
     *
     * @return string
     */
    public function getZitiRouterLinuxBinary()
    {
        return $this->container['ziti_router_linux_binary'];
    }

    /**
     * Sets ziti_router_linux_binary
     *
     * @param string $ziti_router_linux_binary ziti_router_linux_binary
     *
     * @return $this
     */
    public function setZitiRouterLinuxBinary($ziti_router_linux_binary)
    {
        $this->container['ziti_router_linux_binary'] = $ziti_router_linux_binary;

        return $this;
    }

    /**
     * Gets ziti_tunnel_linux_binary_sha_256
     *
     * @return string
     */
    public function getZitiTunnelLinuxBinarySha256()
    {
        return $this->container['ziti_tunnel_linux_binary_sha_256'];
    }

    /**
     * Sets ziti_tunnel_linux_binary_sha_256
     *
     * @param string $ziti_tunnel_linux_binary_sha_256 ziti_tunnel_linux_binary_sha_256
     *
     * @return $this
     */
    public function setZitiTunnelLinuxBinarySha256($ziti_tunnel_linux_binary_sha_256)
    {
        $this->container['ziti_tunnel_linux_binary_sha_256'] = $ziti_tunnel_linux_binary_sha_256;

        return $this;
    }

    /**
     * Gets ziti_android_edge
     *
     * @return string
     */
    public function getZitiAndroidEdge()
    {
        return $this->container['ziti_android_edge'];
    }

    /**
     * Sets ziti_android_edge
     *
     * @param string $ziti_android_edge ziti_android_edge
     *
     * @return $this
     */
    public function setZitiAndroidEdge($ziti_android_edge)
    {
        $this->container['ziti_android_edge'] = $ziti_android_edge;

        return $this;
    }

    /**
     * Gets ziti_tunnel_linux_binary_md5
     *
     * @return string
     */
    public function getZitiTunnelLinuxBinaryMd5()
    {
        return $this->container['ziti_tunnel_linux_binary_md5'];
    }

    /**
     * Sets ziti_tunnel_linux_binary_md5
     *
     * @param string $ziti_tunnel_linux_binary_md5 ziti_tunnel_linux_binary_md5
     *
     * @return $this
     */
    public function setZitiTunnelLinuxBinaryMd5($ziti_tunnel_linux_binary_md5)
    {
        $this->container['ziti_tunnel_linux_binary_md5'] = $ziti_tunnel_linux_binary_md5;

        return $this;
    }

    /**
     * Gets ziti_cli_linux_binary_sha_256
     *
     * @return string
     */
    public function getZitiCliLinuxBinarySha256()
    {
        return $this->container['ziti_cli_linux_binary_sha_256'];
    }

    /**
     * Sets ziti_cli_linux_binary_sha_256
     *
     * @param string $ziti_cli_linux_binary_sha_256 ziti_cli_linux_binary_sha_256
     *
     * @return $this
     */
    public function setZitiCliLinuxBinarySha256($ziti_cli_linux_binary_sha_256)
    {
        $this->container['ziti_cli_linux_binary_sha_256'] = $ziti_cli_linux_binary_sha_256;

        return $this;
    }

    /**
     * Gets active
     *
     * @return bool
     */
    public function getActive()
    {
        return $this->container['active'];
    }

    /**
     * Sets active
     *
     * @param bool $active active
     *
     * @return $this
     */
    public function setActive($active)
    {
        $this->container['active'] = $active;

        return $this;
    }
    /**
     * Returns true if offset exists. False otherwise.
     *
     * @param integer $offset Offset
     *
     * @return boolean
     */
    public function offsetExists($offset)
    {
        return isset($this->container[$offset]);
    }

    /**
     * Gets offset.
     *
     * @param integer $offset Offset
     *
     * @return mixed
     */
    public function offsetGet($offset)
    {
        return isset($this->container[$offset]) ? $this->container[$offset] : null;
    }

    /**
     * Sets value based on offset.
     *
     * @param integer $offset Offset
     * @param mixed   $value  Value to be set
     *
     * @return void
     */
    public function offsetSet($offset, $value)
    {
        if (is_null($offset)) {
            $this->container[] = $value;
        } else {
            $this->container[$offset] = $value;
        }
    }

    /**
     * Unsets offset.
     *
     * @param integer $offset Offset
     *
     * @return void
     */
    public function offsetUnset($offset)
    {
        unset($this->container[$offset]);
    }

    /**
     * Gets the string presentation of the object
     *
     * @return string
     */
    public function __toString()
    {
        return json_encode(
            ObjectSerializer::sanitizeForSerialization($this),
            JSON_PRETTY_PRINT
        );
    }

    /**
     * Gets a header-safe presentation of the object
     *
     * @return string
     */
    public function toHeaderValue()
    {
        return json_encode(ObjectSerializer::sanitizeForSerialization($this));
    }
}


