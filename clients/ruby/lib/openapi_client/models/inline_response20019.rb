=begin
#untitled API

#No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

The version of the OpenAPI document: 5229

Generated by: https://openapi-generator.tech
OpenAPI Generator version: 4.3.1

=end

require 'date'

module OpenapiClient
  class InlineResponse20019
    attr_accessor :_7_3_4

    attr_accessor :_7_3_11

    attr_accessor :_7_3_16

    attr_accessor :_7_1_0

    attr_accessor :_7_3_22

    attr_accessor :_7_3_23

    attr_accessor :_7_3_8

    attr_accessor :_7_3_12

    attr_accessor :_7_2_1

    attr_accessor :_7_3_13

    attr_accessor :_7_0_0

    attr_accessor :_7_3_17

    attr_accessor :_7_3_5

    attr_accessor :_7_3_20

    attr_accessor :_7_3_2

    attr_accessor :_7_3_9

    attr_accessor :_7_3_24

    attr_accessor :_7_2_0

    attr_accessor :_7_3_0

    attr_accessor :_7_3_14

    attr_accessor :_7_3_6

    attr_accessor :_7_3_1

    attr_accessor :_7_3_19

    attr_accessor :_7_3_15

    attr_accessor :_7_3_10

    attr_accessor :_7_3_7

    attr_accessor :_7_3_21

    attr_accessor :_7_3_3

    attr_accessor :_7_3_18

    # Attribute mapping from ruby-style variable name to JSON key.
    def self.attribute_map
      {
        :'_7_3_4' => :'7.3.4',
        :'_7_3_11' => :'7.3.11',
        :'_7_3_16' => :'7.3.16',
        :'_7_1_0' => :'7.1.0',
        :'_7_3_22' => :'7.3.22',
        :'_7_3_23' => :'7.3.23',
        :'_7_3_8' => :'7.3.8',
        :'_7_3_12' => :'7.3.12',
        :'_7_2_1' => :'7.2.1',
        :'_7_3_13' => :'7.3.13',
        :'_7_0_0' => :'7.0.0',
        :'_7_3_17' => :'7.3.17',
        :'_7_3_5' => :'7.3.5',
        :'_7_3_20' => :'7.3.20',
        :'_7_3_2' => :'7.3.2',
        :'_7_3_9' => :'7.3.9',
        :'_7_3_24' => :'7.3.24',
        :'_7_2_0' => :'7.2.0',
        :'_7_3_0' => :'7.3.0',
        :'_7_3_14' => :'7.3.14',
        :'_7_3_6' => :'7.3.6',
        :'_7_3_1' => :'7.3.1',
        :'_7_3_19' => :'7.3.19',
        :'_7_3_15' => :'7.3.15',
        :'_7_3_10' => :'7.3.10',
        :'_7_3_7' => :'7.3.7',
        :'_7_3_21' => :'7.3.21',
        :'_7_3_3' => :'7.3.3',
        :'_7_3_18' => :'7.3.18'
      }
    end

    # Attribute type mapping.
    def self.openapi_types
      {
        :'_7_3_4' => :'InlineResponse20019734',
        :'_7_3_11' => :'InlineResponse20019734',
        :'_7_3_16' => :'InlineResponse200197316',
        :'_7_1_0' => :'InlineResponse20019710',
        :'_7_3_22' => :'InlineResponse200197316',
        :'_7_3_23' => :'InlineResponse200197316',
        :'_7_3_8' => :'InlineResponse20019734',
        :'_7_3_12' => :'InlineResponse20019734',
        :'_7_2_1' => :'InlineResponse20019710',
        :'_7_3_13' => :'InlineResponse20019734',
        :'_7_0_0' => :'InlineResponse20019710',
        :'_7_3_17' => :'InlineResponse200197316',
        :'_7_3_5' => :'InlineResponse20019734',
        :'_7_3_20' => :'InlineResponse200197316',
        :'_7_3_2' => :'InlineResponse20019710',
        :'_7_3_9' => :'InlineResponse20019734',
        :'_7_3_24' => :'InlineResponse200197316',
        :'_7_2_0' => :'InlineResponse20019710',
        :'_7_3_0' => :'InlineResponse20019710',
        :'_7_3_14' => :'InlineResponse200197316',
        :'_7_3_6' => :'InlineResponse20019734',
        :'_7_3_1' => :'InlineResponse20019710',
        :'_7_3_19' => :'InlineResponse200197316',
        :'_7_3_15' => :'InlineResponse200197316',
        :'_7_3_10' => :'InlineResponse20019734',
        :'_7_3_7' => :'InlineResponse20019734',
        :'_7_3_21' => :'InlineResponse200197316',
        :'_7_3_3' => :'InlineResponse20019710',
        :'_7_3_18' => :'InlineResponse200197316'
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
        fail ArgumentError, "The input argument (attributes) must be a hash in `OpenapiClient::InlineResponse20019` initialize method"
      end

      # check to see if the attribute exists and convert string to symbol for hash key
      attributes = attributes.each_with_object({}) { |(k, v), h|
        if (!self.class.attribute_map.key?(k.to_sym))
          fail ArgumentError, "`#{k}` is not a valid attribute in `OpenapiClient::InlineResponse20019`. Please check the name to make sure it's valid. List of attributes: " + self.class.attribute_map.keys.inspect
        end
        h[k.to_sym] = v
      }

      if attributes.key?(:'_7_3_4')
        self._7_3_4 = attributes[:'_7_3_4']
      end

      if attributes.key?(:'_7_3_11')
        self._7_3_11 = attributes[:'_7_3_11']
      end

      if attributes.key?(:'_7_3_16')
        self._7_3_16 = attributes[:'_7_3_16']
      end

      if attributes.key?(:'_7_1_0')
        self._7_1_0 = attributes[:'_7_1_0']
      end

      if attributes.key?(:'_7_3_22')
        self._7_3_22 = attributes[:'_7_3_22']
      end

      if attributes.key?(:'_7_3_23')
        self._7_3_23 = attributes[:'_7_3_23']
      end

      if attributes.key?(:'_7_3_8')
        self._7_3_8 = attributes[:'_7_3_8']
      end

      if attributes.key?(:'_7_3_12')
        self._7_3_12 = attributes[:'_7_3_12']
      end

      if attributes.key?(:'_7_2_1')
        self._7_2_1 = attributes[:'_7_2_1']
      end

      if attributes.key?(:'_7_3_13')
        self._7_3_13 = attributes[:'_7_3_13']
      end

      if attributes.key?(:'_7_0_0')
        self._7_0_0 = attributes[:'_7_0_0']
      end

      if attributes.key?(:'_7_3_17')
        self._7_3_17 = attributes[:'_7_3_17']
      end

      if attributes.key?(:'_7_3_5')
        self._7_3_5 = attributes[:'_7_3_5']
      end

      if attributes.key?(:'_7_3_20')
        self._7_3_20 = attributes[:'_7_3_20']
      end

      if attributes.key?(:'_7_3_2')
        self._7_3_2 = attributes[:'_7_3_2']
      end

      if attributes.key?(:'_7_3_9')
        self._7_3_9 = attributes[:'_7_3_9']
      end

      if attributes.key?(:'_7_3_24')
        self._7_3_24 = attributes[:'_7_3_24']
      end

      if attributes.key?(:'_7_2_0')
        self._7_2_0 = attributes[:'_7_2_0']
      end

      if attributes.key?(:'_7_3_0')
        self._7_3_0 = attributes[:'_7_3_0']
      end

      if attributes.key?(:'_7_3_14')
        self._7_3_14 = attributes[:'_7_3_14']
      end

      if attributes.key?(:'_7_3_6')
        self._7_3_6 = attributes[:'_7_3_6']
      end

      if attributes.key?(:'_7_3_1')
        self._7_3_1 = attributes[:'_7_3_1']
      end

      if attributes.key?(:'_7_3_19')
        self._7_3_19 = attributes[:'_7_3_19']
      end

      if attributes.key?(:'_7_3_15')
        self._7_3_15 = attributes[:'_7_3_15']
      end

      if attributes.key?(:'_7_3_10')
        self._7_3_10 = attributes[:'_7_3_10']
      end

      if attributes.key?(:'_7_3_7')
        self._7_3_7 = attributes[:'_7_3_7']
      end

      if attributes.key?(:'_7_3_21')
        self._7_3_21 = attributes[:'_7_3_21']
      end

      if attributes.key?(:'_7_3_3')
        self._7_3_3 = attributes[:'_7_3_3']
      end

      if attributes.key?(:'_7_3_18')
        self._7_3_18 = attributes[:'_7_3_18']
      end
    end

    # Show invalid properties with the reasons. Usually used together with valid?
    # @return Array for valid properties with the reasons
    def list_invalid_properties
      invalid_properties = Array.new
      if @_7_3_4.nil?
        invalid_properties.push('invalid value for "_7_3_4", _7_3_4 cannot be nil.')
      end

      if @_7_3_11.nil?
        invalid_properties.push('invalid value for "_7_3_11", _7_3_11 cannot be nil.')
      end

      if @_7_3_16.nil?
        invalid_properties.push('invalid value for "_7_3_16", _7_3_16 cannot be nil.')
      end

      if @_7_1_0.nil?
        invalid_properties.push('invalid value for "_7_1_0", _7_1_0 cannot be nil.')
      end

      if @_7_3_22.nil?
        invalid_properties.push('invalid value for "_7_3_22", _7_3_22 cannot be nil.')
      end

      if @_7_3_23.nil?
        invalid_properties.push('invalid value for "_7_3_23", _7_3_23 cannot be nil.')
      end

      if @_7_3_8.nil?
        invalid_properties.push('invalid value for "_7_3_8", _7_3_8 cannot be nil.')
      end

      if @_7_3_12.nil?
        invalid_properties.push('invalid value for "_7_3_12", _7_3_12 cannot be nil.')
      end

      if @_7_2_1.nil?
        invalid_properties.push('invalid value for "_7_2_1", _7_2_1 cannot be nil.')
      end

      if @_7_3_13.nil?
        invalid_properties.push('invalid value for "_7_3_13", _7_3_13 cannot be nil.')
      end

      if @_7_0_0.nil?
        invalid_properties.push('invalid value for "_7_0_0", _7_0_0 cannot be nil.')
      end

      if @_7_3_17.nil?
        invalid_properties.push('invalid value for "_7_3_17", _7_3_17 cannot be nil.')
      end

      if @_7_3_5.nil?
        invalid_properties.push('invalid value for "_7_3_5", _7_3_5 cannot be nil.')
      end

      if @_7_3_20.nil?
        invalid_properties.push('invalid value for "_7_3_20", _7_3_20 cannot be nil.')
      end

      if @_7_3_2.nil?
        invalid_properties.push('invalid value for "_7_3_2", _7_3_2 cannot be nil.')
      end

      if @_7_3_9.nil?
        invalid_properties.push('invalid value for "_7_3_9", _7_3_9 cannot be nil.')
      end

      if @_7_3_24.nil?
        invalid_properties.push('invalid value for "_7_3_24", _7_3_24 cannot be nil.')
      end

      if @_7_2_0.nil?
        invalid_properties.push('invalid value for "_7_2_0", _7_2_0 cannot be nil.')
      end

      if @_7_3_0.nil?
        invalid_properties.push('invalid value for "_7_3_0", _7_3_0 cannot be nil.')
      end

      if @_7_3_14.nil?
        invalid_properties.push('invalid value for "_7_3_14", _7_3_14 cannot be nil.')
      end

      if @_7_3_6.nil?
        invalid_properties.push('invalid value for "_7_3_6", _7_3_6 cannot be nil.')
      end

      if @_7_3_1.nil?
        invalid_properties.push('invalid value for "_7_3_1", _7_3_1 cannot be nil.')
      end

      if @_7_3_19.nil?
        invalid_properties.push('invalid value for "_7_3_19", _7_3_19 cannot be nil.')
      end

      if @_7_3_15.nil?
        invalid_properties.push('invalid value for "_7_3_15", _7_3_15 cannot be nil.')
      end

      if @_7_3_10.nil?
        invalid_properties.push('invalid value for "_7_3_10", _7_3_10 cannot be nil.')
      end

      if @_7_3_7.nil?
        invalid_properties.push('invalid value for "_7_3_7", _7_3_7 cannot be nil.')
      end

      if @_7_3_21.nil?
        invalid_properties.push('invalid value for "_7_3_21", _7_3_21 cannot be nil.')
      end

      if @_7_3_3.nil?
        invalid_properties.push('invalid value for "_7_3_3", _7_3_3 cannot be nil.')
      end

      if @_7_3_18.nil?
        invalid_properties.push('invalid value for "_7_3_18", _7_3_18 cannot be nil.')
      end

      invalid_properties
    end

    # Check to see if the all the properties in the model are valid
    # @return true if the model is valid
    def valid?
      return false if @_7_3_4.nil?
      return false if @_7_3_11.nil?
      return false if @_7_3_16.nil?
      return false if @_7_1_0.nil?
      return false if @_7_3_22.nil?
      return false if @_7_3_23.nil?
      return false if @_7_3_8.nil?
      return false if @_7_3_12.nil?
      return false if @_7_2_1.nil?
      return false if @_7_3_13.nil?
      return false if @_7_0_0.nil?
      return false if @_7_3_17.nil?
      return false if @_7_3_5.nil?
      return false if @_7_3_20.nil?
      return false if @_7_3_2.nil?
      return false if @_7_3_9.nil?
      return false if @_7_3_24.nil?
      return false if @_7_2_0.nil?
      return false if @_7_3_0.nil?
      return false if @_7_3_14.nil?
      return false if @_7_3_6.nil?
      return false if @_7_3_1.nil?
      return false if @_7_3_19.nil?
      return false if @_7_3_15.nil?
      return false if @_7_3_10.nil?
      return false if @_7_3_7.nil?
      return false if @_7_3_21.nil?
      return false if @_7_3_3.nil?
      return false if @_7_3_18.nil?
      true
    end

    # Checks equality by comparing each attribute.
    # @param [Object] Object to be compared
    def ==(o)
      return true if self.equal?(o)
      self.class == o.class &&
          _7_3_4 == o._7_3_4 &&
          _7_3_11 == o._7_3_11 &&
          _7_3_16 == o._7_3_16 &&
          _7_1_0 == o._7_1_0 &&
          _7_3_22 == o._7_3_22 &&
          _7_3_23 == o._7_3_23 &&
          _7_3_8 == o._7_3_8 &&
          _7_3_12 == o._7_3_12 &&
          _7_2_1 == o._7_2_1 &&
          _7_3_13 == o._7_3_13 &&
          _7_0_0 == o._7_0_0 &&
          _7_3_17 == o._7_3_17 &&
          _7_3_5 == o._7_3_5 &&
          _7_3_20 == o._7_3_20 &&
          _7_3_2 == o._7_3_2 &&
          _7_3_9 == o._7_3_9 &&
          _7_3_24 == o._7_3_24 &&
          _7_2_0 == o._7_2_0 &&
          _7_3_0 == o._7_3_0 &&
          _7_3_14 == o._7_3_14 &&
          _7_3_6 == o._7_3_6 &&
          _7_3_1 == o._7_3_1 &&
          _7_3_19 == o._7_3_19 &&
          _7_3_15 == o._7_3_15 &&
          _7_3_10 == o._7_3_10 &&
          _7_3_7 == o._7_3_7 &&
          _7_3_21 == o._7_3_21 &&
          _7_3_3 == o._7_3_3 &&
          _7_3_18 == o._7_3_18
    end

    # @see the `==` method
    # @param [Object] Object to be compared
    def eql?(o)
      self == o
    end

    # Calculates hash code according to all attributes.
    # @return [Integer] Hash code
    def hash
      [_7_3_4, _7_3_11, _7_3_16, _7_1_0, _7_3_22, _7_3_23, _7_3_8, _7_3_12, _7_2_1, _7_3_13, _7_0_0, _7_3_17, _7_3_5, _7_3_20, _7_3_2, _7_3_9, _7_3_24, _7_2_0, _7_3_0, _7_3_14, _7_3_6, _7_3_1, _7_3_19, _7_3_15, _7_3_10, _7_3_7, _7_3_21, _7_3_3, _7_3_18].hash
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
