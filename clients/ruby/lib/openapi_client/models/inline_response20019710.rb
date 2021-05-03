=begin
#untitled API

#No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

The version of the OpenAPI document: 5229

Generated by: https://openapi-generator.tech
OpenAPI Generator version: 4.3.1

=end

require 'date'

module OpenapiClient
  class InlineResponse20019710
    attr_accessor :ziti_cli_linux_binary_sha_1

    attr_accessor :ziti_tunnel_linux_binary

    attr_accessor :ziti_tunnel_linux_binary_sha_1

    attr_accessor :ziti_controller_binary

    attr_accessor :ziti_cli_linux_binary_md5

    attr_accessor :ziti_router_linux_binary_sha_1

    attr_accessor :ziti_router_linux_binary_sha_256

    attr_accessor :ziti_router_linux_binary_md5

    attr_accessor :ziti_windows_desktop_edge

    attr_accessor :ziti_mac_desktop_edge

    attr_accessor :ziti_controller_binary_sha_1

    attr_accessor :ziti_controller_binary_md5

    attr_accessor :ziti_controller_binary_sha_256

    attr_accessor :ziti_ios_edge

    attr_accessor :ziti_cli_linux_binary

    attr_accessor :ziti_version

    attr_accessor :ziti_router_linux_binary

    attr_accessor :ziti_tunnel_linux_binary_sha_256

    attr_accessor :ziti_android_edge

    attr_accessor :ziti_tunnel_linux_binary_md5

    attr_accessor :ziti_cli_linux_binary_sha_256

    attr_accessor :active

    # Attribute mapping from ruby-style variable name to JSON key.
    def self.attribute_map
      {
        :'ziti_cli_linux_binary_sha_1' => :'zitiCliLinuxBinary.sha-1',
        :'ziti_tunnel_linux_binary' => :'zitiTunnelLinuxBinary',
        :'ziti_tunnel_linux_binary_sha_1' => :'zitiTunnelLinuxBinary.sha-1',
        :'ziti_controller_binary' => :'zitiControllerBinary',
        :'ziti_cli_linux_binary_md5' => :'zitiCliLinuxBinary.md5',
        :'ziti_router_linux_binary_sha_1' => :'zitiRouterLinuxBinary.sha-1',
        :'ziti_router_linux_binary_sha_256' => :'zitiRouterLinuxBinary.sha-256',
        :'ziti_router_linux_binary_md5' => :'zitiRouterLinuxBinary.md5',
        :'ziti_windows_desktop_edge' => :'zitiWindowsDesktopEdge',
        :'ziti_mac_desktop_edge' => :'zitiMacDesktopEdge',
        :'ziti_controller_binary_sha_1' => :'zitiControllerBinary.sha-1',
        :'ziti_controller_binary_md5' => :'zitiControllerBinary.md5',
        :'ziti_controller_binary_sha_256' => :'zitiControllerBinary.sha-256',
        :'ziti_ios_edge' => :'zitiIosEdge',
        :'ziti_cli_linux_binary' => :'zitiCliLinuxBinary',
        :'ziti_version' => :'zitiVersion',
        :'ziti_router_linux_binary' => :'zitiRouterLinuxBinary',
        :'ziti_tunnel_linux_binary_sha_256' => :'zitiTunnelLinuxBinary.sha-256',
        :'ziti_android_edge' => :'zitiAndroidEdge',
        :'ziti_tunnel_linux_binary_md5' => :'zitiTunnelLinuxBinary.md5',
        :'ziti_cli_linux_binary_sha_256' => :'zitiCliLinuxBinary.sha-256',
        :'active' => :'active'
      }
    end

    # Attribute type mapping.
    def self.openapi_types
      {
        :'ziti_cli_linux_binary_sha_1' => :'String',
        :'ziti_tunnel_linux_binary' => :'String',
        :'ziti_tunnel_linux_binary_sha_1' => :'String',
        :'ziti_controller_binary' => :'String',
        :'ziti_cli_linux_binary_md5' => :'String',
        :'ziti_router_linux_binary_sha_1' => :'String',
        :'ziti_router_linux_binary_sha_256' => :'String',
        :'ziti_router_linux_binary_md5' => :'String',
        :'ziti_windows_desktop_edge' => :'String',
        :'ziti_mac_desktop_edge' => :'String',
        :'ziti_controller_binary_sha_1' => :'String',
        :'ziti_controller_binary_md5' => :'String',
        :'ziti_controller_binary_sha_256' => :'String',
        :'ziti_ios_edge' => :'String',
        :'ziti_cli_linux_binary' => :'String',
        :'ziti_version' => :'String',
        :'ziti_router_linux_binary' => :'String',
        :'ziti_tunnel_linux_binary_sha_256' => :'String',
        :'ziti_android_edge' => :'String',
        :'ziti_tunnel_linux_binary_md5' => :'String',
        :'ziti_cli_linux_binary_sha_256' => :'String',
        :'active' => :'Boolean'
      }
    end

    # List of attributes with nullable: true
    def self.openapi_nullable
      Set.new([
      ])
    end

    # Initializes the object
    # @param [Hash] attributes Model attributes in the form of hash
    def initialize(attributes = {})
      if (!attributes.is_a?(Hash))
        fail ArgumentError, "The input argument (attributes) must be a hash in `OpenapiClient::InlineResponse20019710` initialize method"
      end

      # check to see if the attribute exists and convert string to symbol for hash key
      attributes = attributes.each_with_object({}) { |(k, v), h|
        if (!self.class.attribute_map.key?(k.to_sym))
          fail ArgumentError, "`#{k}` is not a valid attribute in `OpenapiClient::InlineResponse20019710`. Please check the name to make sure it's valid. List of attributes: " + self.class.attribute_map.keys.inspect
        end
        h[k.to_sym] = v
      }

      if attributes.key?(:'ziti_cli_linux_binary_sha_1')
        self.ziti_cli_linux_binary_sha_1 = attributes[:'ziti_cli_linux_binary_sha_1']
      end

      if attributes.key?(:'ziti_tunnel_linux_binary')
        self.ziti_tunnel_linux_binary = attributes[:'ziti_tunnel_linux_binary']
      end

      if attributes.key?(:'ziti_tunnel_linux_binary_sha_1')
        self.ziti_tunnel_linux_binary_sha_1 = attributes[:'ziti_tunnel_linux_binary_sha_1']
      end

      if attributes.key?(:'ziti_controller_binary')
        self.ziti_controller_binary = attributes[:'ziti_controller_binary']
      end

      if attributes.key?(:'ziti_cli_linux_binary_md5')
        self.ziti_cli_linux_binary_md5 = attributes[:'ziti_cli_linux_binary_md5']
      end

      if attributes.key?(:'ziti_router_linux_binary_sha_1')
        self.ziti_router_linux_binary_sha_1 = attributes[:'ziti_router_linux_binary_sha_1']
      end

      if attributes.key?(:'ziti_router_linux_binary_sha_256')
        self.ziti_router_linux_binary_sha_256 = attributes[:'ziti_router_linux_binary_sha_256']
      end

      if attributes.key?(:'ziti_router_linux_binary_md5')
        self.ziti_router_linux_binary_md5 = attributes[:'ziti_router_linux_binary_md5']
      end

      if attributes.key?(:'ziti_windows_desktop_edge')
        self.ziti_windows_desktop_edge = attributes[:'ziti_windows_desktop_edge']
      end

      if attributes.key?(:'ziti_mac_desktop_edge')
        self.ziti_mac_desktop_edge = attributes[:'ziti_mac_desktop_edge']
      end

      if attributes.key?(:'ziti_controller_binary_sha_1')
        self.ziti_controller_binary_sha_1 = attributes[:'ziti_controller_binary_sha_1']
      end

      if attributes.key?(:'ziti_controller_binary_md5')
        self.ziti_controller_binary_md5 = attributes[:'ziti_controller_binary_md5']
      end

      if attributes.key?(:'ziti_controller_binary_sha_256')
        self.ziti_controller_binary_sha_256 = attributes[:'ziti_controller_binary_sha_256']
      end

      if attributes.key?(:'ziti_ios_edge')
        self.ziti_ios_edge = attributes[:'ziti_ios_edge']
      end

      if attributes.key?(:'ziti_cli_linux_binary')
        self.ziti_cli_linux_binary = attributes[:'ziti_cli_linux_binary']
      end

      if attributes.key?(:'ziti_version')
        self.ziti_version = attributes[:'ziti_version']
      end

      if attributes.key?(:'ziti_router_linux_binary')
        self.ziti_router_linux_binary = attributes[:'ziti_router_linux_binary']
      end

      if attributes.key?(:'ziti_tunnel_linux_binary_sha_256')
        self.ziti_tunnel_linux_binary_sha_256 = attributes[:'ziti_tunnel_linux_binary_sha_256']
      end

      if attributes.key?(:'ziti_android_edge')
        self.ziti_android_edge = attributes[:'ziti_android_edge']
      end

      if attributes.key?(:'ziti_tunnel_linux_binary_md5')
        self.ziti_tunnel_linux_binary_md5 = attributes[:'ziti_tunnel_linux_binary_md5']
      end

      if attributes.key?(:'ziti_cli_linux_binary_sha_256')
        self.ziti_cli_linux_binary_sha_256 = attributes[:'ziti_cli_linux_binary_sha_256']
      end

      if attributes.key?(:'active')
        self.active = attributes[:'active']
      end
    end

    # Show invalid properties with the reasons. Usually used together with valid?
    # @return Array for valid properties with the reasons
    def list_invalid_properties
      invalid_properties = Array.new
      if @ziti_cli_linux_binary_sha_1.nil?
        invalid_properties.push('invalid value for "ziti_cli_linux_binary_sha_1", ziti_cli_linux_binary_sha_1 cannot be nil.')
      end

      if @ziti_tunnel_linux_binary.nil?
        invalid_properties.push('invalid value for "ziti_tunnel_linux_binary", ziti_tunnel_linux_binary cannot be nil.')
      end

      if @ziti_tunnel_linux_binary_sha_1.nil?
        invalid_properties.push('invalid value for "ziti_tunnel_linux_binary_sha_1", ziti_tunnel_linux_binary_sha_1 cannot be nil.')
      end

      if @ziti_controller_binary.nil?
        invalid_properties.push('invalid value for "ziti_controller_binary", ziti_controller_binary cannot be nil.')
      end

      if @ziti_cli_linux_binary_md5.nil?
        invalid_properties.push('invalid value for "ziti_cli_linux_binary_md5", ziti_cli_linux_binary_md5 cannot be nil.')
      end

      if @ziti_router_linux_binary_sha_1.nil?
        invalid_properties.push('invalid value for "ziti_router_linux_binary_sha_1", ziti_router_linux_binary_sha_1 cannot be nil.')
      end

      if @ziti_router_linux_binary_sha_256.nil?
        invalid_properties.push('invalid value for "ziti_router_linux_binary_sha_256", ziti_router_linux_binary_sha_256 cannot be nil.')
      end

      if @ziti_router_linux_binary_md5.nil?
        invalid_properties.push('invalid value for "ziti_router_linux_binary_md5", ziti_router_linux_binary_md5 cannot be nil.')
      end

      if @ziti_windows_desktop_edge.nil?
        invalid_properties.push('invalid value for "ziti_windows_desktop_edge", ziti_windows_desktop_edge cannot be nil.')
      end

      if @ziti_mac_desktop_edge.nil?
        invalid_properties.push('invalid value for "ziti_mac_desktop_edge", ziti_mac_desktop_edge cannot be nil.')
      end

      if @ziti_controller_binary_sha_1.nil?
        invalid_properties.push('invalid value for "ziti_controller_binary_sha_1", ziti_controller_binary_sha_1 cannot be nil.')
      end

      if @ziti_controller_binary_md5.nil?
        invalid_properties.push('invalid value for "ziti_controller_binary_md5", ziti_controller_binary_md5 cannot be nil.')
      end

      if @ziti_controller_binary_sha_256.nil?
        invalid_properties.push('invalid value for "ziti_controller_binary_sha_256", ziti_controller_binary_sha_256 cannot be nil.')
      end

      if @ziti_ios_edge.nil?
        invalid_properties.push('invalid value for "ziti_ios_edge", ziti_ios_edge cannot be nil.')
      end

      if @ziti_cli_linux_binary.nil?
        invalid_properties.push('invalid value for "ziti_cli_linux_binary", ziti_cli_linux_binary cannot be nil.')
      end

      if @ziti_version.nil?
        invalid_properties.push('invalid value for "ziti_version", ziti_version cannot be nil.')
      end

      if @ziti_router_linux_binary.nil?
        invalid_properties.push('invalid value for "ziti_router_linux_binary", ziti_router_linux_binary cannot be nil.')
      end

      if @ziti_tunnel_linux_binary_sha_256.nil?
        invalid_properties.push('invalid value for "ziti_tunnel_linux_binary_sha_256", ziti_tunnel_linux_binary_sha_256 cannot be nil.')
      end

      if @ziti_android_edge.nil?
        invalid_properties.push('invalid value for "ziti_android_edge", ziti_android_edge cannot be nil.')
      end

      if @ziti_tunnel_linux_binary_md5.nil?
        invalid_properties.push('invalid value for "ziti_tunnel_linux_binary_md5", ziti_tunnel_linux_binary_md5 cannot be nil.')
      end

      if @ziti_cli_linux_binary_sha_256.nil?
        invalid_properties.push('invalid value for "ziti_cli_linux_binary_sha_256", ziti_cli_linux_binary_sha_256 cannot be nil.')
      end

      if @active.nil?
        invalid_properties.push('invalid value for "active", active cannot be nil.')
      end

      invalid_properties
    end

    # Check to see if the all the properties in the model are valid
    # @return true if the model is valid
    def valid?
      return false if @ziti_cli_linux_binary_sha_1.nil?
      return false if @ziti_tunnel_linux_binary.nil?
      return false if @ziti_tunnel_linux_binary_sha_1.nil?
      return false if @ziti_controller_binary.nil?
      return false if @ziti_cli_linux_binary_md5.nil?
      return false if @ziti_router_linux_binary_sha_1.nil?
      return false if @ziti_router_linux_binary_sha_256.nil?
      return false if @ziti_router_linux_binary_md5.nil?
      return false if @ziti_windows_desktop_edge.nil?
      return false if @ziti_mac_desktop_edge.nil?
      return false if @ziti_controller_binary_sha_1.nil?
      return false if @ziti_controller_binary_md5.nil?
      return false if @ziti_controller_binary_sha_256.nil?
      return false if @ziti_ios_edge.nil?
      return false if @ziti_cli_linux_binary.nil?
      return false if @ziti_version.nil?
      return false if @ziti_router_linux_binary.nil?
      return false if @ziti_tunnel_linux_binary_sha_256.nil?
      return false if @ziti_android_edge.nil?
      return false if @ziti_tunnel_linux_binary_md5.nil?
      return false if @ziti_cli_linux_binary_sha_256.nil?
      return false if @active.nil?
      true
    end

    # Checks equality by comparing each attribute.
    # @param [Object] Object to be compared
    def ==(o)
      return true if self.equal?(o)
      self.class == o.class &&
          ziti_cli_linux_binary_sha_1 == o.ziti_cli_linux_binary_sha_1 &&
          ziti_tunnel_linux_binary == o.ziti_tunnel_linux_binary &&
          ziti_tunnel_linux_binary_sha_1 == o.ziti_tunnel_linux_binary_sha_1 &&
          ziti_controller_binary == o.ziti_controller_binary &&
          ziti_cli_linux_binary_md5 == o.ziti_cli_linux_binary_md5 &&
          ziti_router_linux_binary_sha_1 == o.ziti_router_linux_binary_sha_1 &&
          ziti_router_linux_binary_sha_256 == o.ziti_router_linux_binary_sha_256 &&
          ziti_router_linux_binary_md5 == o.ziti_router_linux_binary_md5 &&
          ziti_windows_desktop_edge == o.ziti_windows_desktop_edge &&
          ziti_mac_desktop_edge == o.ziti_mac_desktop_edge &&
          ziti_controller_binary_sha_1 == o.ziti_controller_binary_sha_1 &&
          ziti_controller_binary_md5 == o.ziti_controller_binary_md5 &&
          ziti_controller_binary_sha_256 == o.ziti_controller_binary_sha_256 &&
          ziti_ios_edge == o.ziti_ios_edge &&
          ziti_cli_linux_binary == o.ziti_cli_linux_binary &&
          ziti_version == o.ziti_version &&
          ziti_router_linux_binary == o.ziti_router_linux_binary &&
          ziti_tunnel_linux_binary_sha_256 == o.ziti_tunnel_linux_binary_sha_256 &&
          ziti_android_edge == o.ziti_android_edge &&
          ziti_tunnel_linux_binary_md5 == o.ziti_tunnel_linux_binary_md5 &&
          ziti_cli_linux_binary_sha_256 == o.ziti_cli_linux_binary_sha_256 &&
          active == o.active
    end

    # @see the `==` method
    # @param [Object] Object to be compared
    def eql?(o)
      self == o
    end

    # Calculates hash code according to all attributes.
    # @return [Integer] Hash code
    def hash
      [ziti_cli_linux_binary_sha_1, ziti_tunnel_linux_binary, ziti_tunnel_linux_binary_sha_1, ziti_controller_binary, ziti_cli_linux_binary_md5, ziti_router_linux_binary_sha_1, ziti_router_linux_binary_sha_256, ziti_router_linux_binary_md5, ziti_windows_desktop_edge, ziti_mac_desktop_edge, ziti_controller_binary_sha_1, ziti_controller_binary_md5, ziti_controller_binary_sha_256, ziti_ios_edge, ziti_cli_linux_binary, ziti_version, ziti_router_linux_binary, ziti_tunnel_linux_binary_sha_256, ziti_android_edge, ziti_tunnel_linux_binary_md5, ziti_cli_linux_binary_sha_256, active].hash
    end

    # Builds the object from hash
    # @param [Hash] attributes Model attributes in the form of hash
    # @return [Object] Returns the model itself
    def self.build_from_hash(attributes)
      new.build_from_hash(attributes)
    end

    # Builds the object from hash
    # @param [Hash] attributes Model attributes in the form of hash
    # @return [Object] Returns the model itself
    def build_from_hash(attributes)
      return nil unless attributes.is_a?(Hash)
      self.class.openapi_types.each_pair do |key, type|
        if type =~ /\AArray<(.*)>/i
          # check to ensure the input is an array given that the attribute
          # is documented as an array but the input is not
          if attributes[self.class.attribute_map[key]].is_a?(Array)
            self.send("#{key}=", attributes[self.class.attribute_map[key]].map { |v| _deserialize($1, v) })
          end
        elsif !attributes[self.class.attribute_map[key]].nil?
          self.send("#{key}=", _deserialize(type, attributes[self.class.attribute_map[key]]))
        end # or else data not found in attributes(hash), not an issue as the data can be optional
      end

      self
    end

    # Deserializes the data based on type
    # @param string type Data type
    # @param string value Value to be deserialized
    # @return [Object] Deserialized data
    def _deserialize(type, value)
      case type.to_sym
      when :DateTime
        DateTime.parse(value)
      when :Date
        Date.parse(value)
      when :String
        value.to_s
      when :Integer
        value.to_i
      when :Float
        value.to_f
      when :Boolean
        if value.to_s =~ /\A(true|t|yes|y|1)\z/i
          true
        else
          false
        end
      when :Object
        # generic object (usually a Hash), return directly
        value
      when /\AArray<(?<inner_type>.+)>\z/
        inner_type = Regexp.last_match[:inner_type]
        value.map { |v| _deserialize(inner_type, v) }
      when /\AHash<(?<k_type>.+?), (?<v_type>.+)>\z/
        k_type = Regexp.last_match[:k_type]
        v_type = Regexp.last_match[:v_type]
        {}.tap do |hash|
          value.each do |k, v|
            hash[_deserialize(k_type, k)] = _deserialize(v_type, v)
          end
        end
      else # model
        OpenapiClient.const_get(type).build_from_hash(value)
      end
    end

    # Returns the string representation of the object
    # @return [String] String presentation of the object
    def to_s
      to_hash.to_s
    end

    # to_body is an alias to to_hash (backward compatibility)
    # @return [Hash] Returns the object in the form of hash
    def to_body
      to_hash
    end

    # Returns the object in the form of hash
    # @return [Hash] Returns the object in the form of hash
    def to_hash
      hash = {}
      self.class.attribute_map.each_pair do |attr, param|
        value = self.send(attr)
        if value.nil?
          is_nullable = self.class.openapi_nullable.include?(attr)
          next if !is_nullable || (is_nullable && !instance_variable_defined?(:"@#{attr}"))
        end
        
        hash[param] = _to_hash(value)
      end
      hash
    end

    # Outputs non-array value in the form of hash
    # For object, use to_hash. Otherwise, just return the value
    # @param [Object] value Any valid value
    # @return [Hash] Returns the value in the form of hash
    def _to_hash(value)
      if value.is_a?(Array)
        value.compact.map { |v| _to_hash(v) }
      elsif value.is_a?(Hash)
        {}.tap do |hash|
          value.each { |k, v| hash[k] = _to_hash(v) }
        end
      elsif value.respond_to? :to_hash
        value.to_hash
      else
        value
      end
    end
  end
end
